"""
health_check.py
--------------------
System health check for the Makaton Gesture Recognition Tool.

This script checks:
- Python version
- OpenCV installation and version
- MediaPipe availability
- Config file loading
- Logging setup
- Webcam availability
- A quick FPS smoke test over a small number of frames

Usage:
    python health_check.py
"""

from __future__ import annotations

import logging
import sys
import time
from pathlib import Path

try:
    import cv2
except ImportError:  # pragma: no cover
    cv2 = None  # type: ignore[assignment]

try:
    import mediapipe as mp
except ImportError:  # pragma: no cover
    mp = None  # type: ignore[assignment]

try:
    from logging_config import setup_logging
except ImportError:  # pragma: no cover
    setup_logging = None  # type: ignore[assignment]

try:
    from config_loader import load_config
except ImportError:  # pragma: no cover
    load_config = None  # type: ignore[assignment]


def setup_logger() -> logging.Logger:
    if setup_logging is not None:
        setup_logging()
    else:
        logging.basicConfig(
            level=logging.INFO,
            format="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
        )
    return logging.getLogger(__name__)


def print_status(label: str, ok: bool, details: str | None = None) -> None:
    prefix = "[OK] " if ok else "[FAIL]"
    line = f"{prefix} {label}"
    if details:
        line += f" - {details}"
    print(line)


def check_python_version(logger: logging.Logger) -> bool:
    major, minor = sys.version_info[:2]
    ok = major == 3 and minor >= 10
    details = f"Python {major}.{minor} detected (>= 3.10 required)"
    logger.info(details)
    print_status("Python version", ok, details)
    return ok


def check_opencv(logger: logging.Logger) -> bool:
    if cv2 is None:
        logger.error("OpenCV (cv2) is not installed")
        print_status("OpenCV", False, "cv2 not importable")
        return False
    version = getattr(cv2, "__version__", "unknown")
    details = f"OpenCV version {version}"
    logger.info(details)
    print_status("OpenCV", True, details)
    return True


def check_mediapipe(logger: logging.Logger) -> bool:
    if mp is None:
        logger.error("Mediapipe is not installed")
        print_status("MediaPipe", False, "mediapipe not importable")
        return False
    try:
        _ = mp.solutions.hands.Hands
        details = "MediaPipe Hands solution available"
        logger.info(details)
        print_status("MediaPipe", True, details)
        return True
    except Exception as exc:  # pragma: no cover
        logger.exception("Error while checking Mediapipe: %s", exc)
        print_status("MediaPipe", False, "Hands solution not available")
        return False


def check_config(logger: logging.Logger) -> bool:
    if load_config is None:
        print_status("Config loader", False, "config_loader not importable")
        logger.error("config_loader.load_config not available")
        return False

    config_path = Path("config.yaml")
    if not config_path.exists():
        print_status("Config file", False, "config.yaml not found")
        logger.error("config.yaml file not found")
        return False

    try:
        config = load_config(config_path)
    except Exception as exc:  # pragma: no cover
        logger.exception("Error loading config.yaml: %s", exc)
        print_status("Config file", False, "failed to parse config.yaml")
        return False

    details = (
        f"camera_index={config.camera.index}, " f"refresh_ms={config.gui.refresh_ms}"
    )
    logger.info("Config loaded successfully: %s", details)
    print_status("Config file", True, details)
    return True


def check_logging_dir(logger: logging.Logger) -> bool:
    logs_dir = Path("logs")
    try:
        logs_dir.mkdir(exist_ok=True)
        test_file = logs_dir / "health_check_test.log"
        with test_file.open("w", encoding="utf-8") as f:
            f.write("health check\n")
        test_file.unlink(missing_ok=True)
        print_status("Logging directory", True, f"logs/ usable at {logs_dir}")
        logger.info("Logging directory %s is usable", logs_dir)
        return True
    except Exception as exc:  # pragma: no cover
        logger.exception("Logging directory not usable: %s", exc)
        print_status("Logging directory", False, "cannot write to logs/")
        return False


def check_webcam(logger: logging.Logger, camera_index: int = 0) -> tuple[bool, int]:
    if cv2 is None:
        print_status("Webcam", False, "cv2 not available")
        return False, camera_index

    cap = cv2.VideoCapture(camera_index)
    if not cap.isOpened():
        logger.error("Failed to open webcam at index %s", camera_index)
        print_status("Webcam", False, f"cannot open camera index {camera_index}")
        return False, camera_index

    ok, _ = cap.read()
    cap.release()

    if not ok:
        logger.error("Webcam opened but failed to read a frame")
        print_status("Webcam", False, "unable to read frame from webcam")
        return False, camera_index

    print_status("Webcam", True, f"camera index {camera_index} readable")
    logger.info("Webcam at index %s is available and readable", camera_index)
    return True, camera_index


def quick_fps_smoke_test(logger: logging.Logger, camera_index: int = 0) -> bool:
    """
    Run a very small FPS test over a limited number of frames
    to confirm basic real-time performance.
    """
    if cv2 is None or mp is None:
        print_status("FPS smoke test", False, "cv2 or mediapipe unavailable")
        return False

    num_frames = 50
    cap = cv2.VideoCapture(camera_index)
    if not cap.isOpened():
        print_status("FPS smoke test", False, "cannot open webcam")
        return False

    mp_hands = mp.solutions.hands
    hands = mp_hands.Hands(max_num_hands=1)

    frame_count = 0
    start_time = time.perf_counter()

    while frame_count < num_frames:
        ok, frame = cap.read()
        if not ok:
            logger.warning("Failed to read frame %s during FPS smoke test", frame_count)
            break

        # BGR -> RGB
        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        _ = hands.process(rgb)
        frame_count += 1

    end_time = time.perf_counter()
    cap.release()
    hands.close()

    if frame_count == 0:
        print_status("FPS smoke test", False, "no frames processed")
        logger.error("No frames processed during FPS smoke test")
        return False

    total_time = end_time - start_time
    fps = frame_count / total_time if total_time > 0 else 0.0

    logger.info(
        "FPS smoke test: frames=%s total_time=%.3f fps=%.2f",
        frame_count,
        total_time,
        fps,
    )
    print_status(
        "FPS smoke test",
        True,
        f"{fps:.2f} FPS over {frame_count} frames",
    )
    return True


def main() -> None:
    print("\n=== Makaton Gesture Recognition Tool – Health Check ===\n")

    logger = setup_logger()

    overall_ok = True

    overall_ok &= check_python_version(logger)
    overall_ok &= check_opencv(logger)
    overall_ok &= check_mediapipe(logger)
    overall_ok &= check_config(logger)
    overall_ok &= check_logging_dir(logger)

    # Try primary webcam index 0 (aligned with config default)
    webcam_ok, cam_index = check_webcam(logger, camera_index=0)
    overall_ok &= webcam_ok

    fps_ok = quick_fps_smoke_test(logger, camera_index=cam_index)
    overall_ok &= fps_ok

    print("\n=== Health Check Summary ===")
    if overall_ok:
        print("✅ All critical checks passed. System is ready to run the tool.")
        logger.info("Health check passed: system ready")
        sys.exit(0)
    else:
        print("⚠ Some checks failed. Please review the messages above.")
        logger.warning("Health check completed with failures")
        sys.exit(1)


if __name__ == "__main__":
    main()
