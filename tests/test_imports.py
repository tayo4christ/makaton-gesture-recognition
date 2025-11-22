"""
Basic smoke tests for the Makaton Gesture Recognition Tool.

These tests ensure that the main modules can be imported
without raising errors. This is a foundation for future,
more detailed tests.
"""

import importlib


def test_makaton_module_imports() -> None:
    """Ensure the main application module can be imported."""
    module_name = "makaton_gesture_recognition"
    module = importlib.import_module(module_name)
    assert module is not None
