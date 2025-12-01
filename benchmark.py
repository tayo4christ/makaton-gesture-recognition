"""
Performance benchmarking script for the Makaton Gesture Recognition Tool.

This script measures:
- End-to-end frame processing time (OpenCV + MediaPipe)
- Approximate frames per second (FPS) over N frames

Usage:
    python benchmark.py
"""

from __future__ import annotations

import logging
import statistics
import time
from dataclasses import dataclass

import cv2
import mediapipe as mp

try:
    from logging_config import setup_logging
except ImportError:
    setup_logging = None  # Fallback: use basicConfig


@dataclass
class BenchmarkConfig:
    num_frames: int = 200
    camera_index: int = 0


def setup_logger() -> logging.Logger:
    if setup_logging is not None:
        setup_logging()
    else:
        logging.basicConfig(
            level=logging.INFO,
            format="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
        )
    logger = logging.getLogger(__name__)
    return logger


def run_benchmark(config: BenchmarkConfig, logger: logging.Logger) -> None:
    mp_hands = mp.solutions.hands
    hands = mp_hands.Hands(max_num_hands=1)

    cap = cv2.VideoCapture(config.camera_index)
    if not cap.isOpened():
        logger.error("Failed to open webcam on index %s", config.camera_index)
        return

    logger.info(
        "Starting benchmark for %s frames on camera index %s",
        config.num_frames,
        config.camera_index,
    )

    frame_times: list[float] = []
    processed_frames = 0

    while processed_frames < config.num_frames:
        start_time = time.perf_counter()

        ok, frame = cap.read()
        if not ok:
            logger.warning("Failed to read frame %s from webcam", processed_frames)
            break

        # Convert BGR -> RGB for MediaPipe
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # Run hand landmark detection
        _ = hands.process(rgb_frame)

        end_time = time.perf_counter()
        frame_time = end_time - start_time
        frame_times.append(frame_time)
        processed_frames += 1

    cap.release()
    hands.close()

    if not frame_times:
        logger.error("No frames processed, benchmark aborted.")
        return

    avg_time = statistics.mean(frame_times)
    median_time = statistics.median(frame_times)
    min_time = min(frame_times)
    max_time = max(frame_times)
    fps = 1.0 / avg_time if avg_time > 0 else 0.0

    logger.info("Benchmark complete:")
    logger.info("  Frames processed: %s", processed_frames)
    logger.info("  Average frame time: %.4f s", avg_time)
    logger.info("  Median frame time: %.4f s", median_time)
    logger.info("  Min frame time: %.4f s", min_time)
    logger.info("  Max frame time: %.4f s", max_time)
    logger.info("  Approx FPS: %.2f", fps)

    print("\n=== Makaton Gesture Recognition Benchmark ===")
    print(f"Frames processed: {processed_frames}")
    print(f"Average frame time: {avg_time:.4f} s")
    print(f"Median frame time:  {median_time:.4f} s")
    print(f"Min frame time:     {min_time:.4f} s")
    print(f"Max frame time:     {max_time:.4f} s")
    print(f"Approx FPS:         {fps:.2f}")


def main() -> None:
    logger = setup_logger()
    config = BenchmarkConfig()
    run_benchmark(config, logger)


if __name__ == "__main__":
    main()
