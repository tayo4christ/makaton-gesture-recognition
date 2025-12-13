"""
Unit tests for health_check.py.

These tests focus on logic that can be validated without requiring a real webcam.
We monkeypatch dependencies (cv2, mediapipe, config loader) to keep CI reliable.
"""

from __future__ import annotations

import types

import health_check


class DummyLogger:
    def info(self, *args, **kwargs): ...
    def warning(self, *args, **kwargs): ...
    def error(self, *args, **kwargs): ...
    def exception(self, *args, **kwargs): ...


def test_print_status_ok(capsys):
    health_check.print_status("Example", True, "details")
    out = capsys.readouterr().out
    assert "[OK]" in out
    assert "Example" in out
    assert "details" in out


def test_print_status_fail(capsys):
    health_check.print_status("Example", False, "details")
    out = capsys.readouterr().out
    assert "[FAIL]" in out
    assert "Example" in out


def test_check_opencv_missing(monkeypatch, capsys):
    monkeypatch.setattr(health_check, "cv2", None)
    ok = health_check.check_opencv(DummyLogger())
    out = capsys.readouterr().out
    assert ok is False
    assert "OpenCV" in out
    assert "[FAIL]" in out


def test_check_mediapipe_missing(monkeypatch, capsys):
    monkeypatch.setattr(health_check, "mp", None)
    ok = health_check.check_mediapipe(DummyLogger())
    out = capsys.readouterr().out
    assert ok is False
    assert "MediaPipe" in out
    assert "[FAIL]" in out


def test_check_config_loader_missing(monkeypatch, capsys):
    monkeypatch.setattr(health_check, "load_config", None)
    ok = health_check.check_config(DummyLogger())
    out = capsys.readouterr().out
    assert ok is False
    assert "Config loader" in out
    assert "[FAIL]" in out


def test_check_config_file_missing(monkeypatch, tmp_path, capsys):
    """
    Ensure check_config fails gracefully when config.yaml does not exist.
    """
    # Make config loader exist, but point cwd to temp dir without config.yaml
    monkeypatch.setattr(health_check, "load_config", lambda _: None)

    # Patch Path("config.yaml") resolution by changing working directory
    monkeypatch.chdir(tmp_path)

    ok = health_check.check_config(DummyLogger())
    out = capsys.readouterr().out
    assert ok is False
    assert "Config file" in out
    assert "not found" in out


def test_check_mediapipe_available(monkeypatch, capsys):
    """
    Simulate mediapipe.solutions.hands.Hands being present.
    """
    fake_mp = types.SimpleNamespace(
        solutions=types.SimpleNamespace(
            hands=types.SimpleNamespace(Hands=object),
        )
    )
    monkeypatch.setattr(health_check, "mp", fake_mp)

    ok = health_check.check_mediapipe(DummyLogger())
    out = capsys.readouterr().out
    assert ok is True
    assert "[OK]" in out
