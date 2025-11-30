"""
Unit tests for the rule-based gesture recogniser.

These tests use simple mock landmarks (x, y only) that approximate the
conditions in `recognize_gesture`.
"""

from __future__ import annotations

from dataclasses import dataclass

from makaton_gesture_recognition import (
    recognize_gesture,
)


# Mediapipe landmarks are objects with x, y (and z) attributes.
# For testing we only need x and y, so we create a lightweight mock.
@dataclass
class MockLandmark:
    x: float
    y: float


def make_landmarks(overrides: dict[int, tuple[float, float]]) -> list[MockLandmark]:
    """
    Create a full list of 21 landmarks.

    `overrides` is a mapping from index -> (x, y). Any index not provided
    defaults to (0.0, 0.0).
    """
    points = [MockLandmark(0.0, 0.0) for _ in range(21)]
    for idx, (x, y) in overrides.items():
        points[idx] = MockLandmark(x, y)
    return points


def test_recognize_hello_all_fingers_extended():
    """
    When the thumb is far from all fingertips, the gesture should be 'Hello'.
    """
    # 0 = wrist, 4 = thumb_tip, 8/12/16/20 = fingertips
    landmarks = make_landmarks(
        {
            0: (0.0, 0.0),  # wrist
            4: (0.0, 0.0),  # thumb_tip
            8: (1.0, 0.0),  # index_tip
            12: (1.0, 0.5),  # middle_tip
            16: (1.0, 1.0),  # ring_tip
            20: (0.5, 1.0),  # pinky_tip
        }
    )
    gesture = recognize_gesture(landmarks)
    assert gesture == "Hello"


def test_recognize_goodbye_fingers_close_together():
    """
    When all fingertips are very close to the thumb, the gesture should be 'Goodbye'.
    """
    # thumb and all fingertips clustered together to satisfy the
    # GOODBYE_MAX_DIST threshold.
    landmarks = make_landmarks(
        {
            0: (0.0, 0.0),
            4: (0.5, 0.5),
            8: (0.51, 0.5),
            12: (0.52, 0.5),
            16: (0.49, 0.5),
            20: (0.5, 0.51),
        }
    )
    gesture = recognize_gesture(landmarks)
    assert gesture == "Goodbye"


def test_recognize_yes_thumb_to_left_of_index_without_other_rules_matching():
    """
    When neither the 'Hello' nor 'Goodbye' distance rules match but the thumb
    is to the left of the index finger, the recogniser should return 'Yes'.
    """
    # Set distances so:
    # - Not all > HELLO_MIN_DIST
    # - Not all < GOODBYE_MAX_DIST
    # - Thumb is to the left of index (thumb.x < index.x)
    # - Wrist->thumb distance is greater than wrist->index distance so that
    #   'Please' / 'Thank You' rules do not trigger.
    landmarks = make_landmarks(
        {
            0: (0.0, 0.0),  # wrist
            4: (0.4, 0.6),  # thumb_tip
            8: (0.6, 0.3),  # index_tip (to the right of thumb)
            12: (0.41, 0.6),  # other fingertips very close to thumb
            16: (0.39, 0.6),
            20: (0.4, 0.59),
        }
    )

    gesture = recognize_gesture(landmarks)
    assert gesture == "Yes"


def test_no_gesture_when_rules_do_not_match():
    """
    When distances do not satisfy any of the rule conditions,
    the recogniser should return None.
    """
    # Choose values such that:
    # - thumb-index distance is between GOODBYE_MAX_DIST and HELLO_MIN_DIST
    #   (so neither 'Hello' nor 'Goodbye' fire)
    # - wrist->thumb distance >= wrist->index distance
    #   (so 'Please' / 'Thank You' rules do not fire)
    # - thumb.x >= index.x (so 'Yes' rule does not fire)
    landmarks = make_landmarks(
        {
            0: (0.0, 0.0),  # wrist
            4: (0.4, 0.0),  # thumb_tip
            8: (0.2, 0.0),  # index_tip (to the left of thumb)
            12: (0.4, 0.2),
            16: (0.4, -0.2),
            20: (0.4, 0.1),
        }
    )

    gesture = recognize_gesture(landmarks)
    assert gesture is None
