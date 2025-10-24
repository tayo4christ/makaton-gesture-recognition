import tkinter as tk

import cv2
import mediapipe as mp
import numpy as np
from PIL import Image, ImageTk

# -----------------------------
# Setup
# -----------------------------

# Initialize Mediapipe hands module
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(max_num_hands=1)
mp_drawing = mp.solutions.drawing_utils

# Video capture handle (created when "Start Video" is pressed)
cap = None

# Define the gesture descriptions
GESTURE_DESCRIPTIONS = {
    "Hello": "Open hand, palm facing forward, all fingers extended.",
    "Goodbye": "Open hand, palm facing forward, moving fingers as if waving.",
    "Please": "Flat hand, palm facing up, moving in a small circular motion.",
    "Thank You": "Flat hand, palm facing up, moving away from the chin.",
    "Yes": "Fist with thumb up.",
}


# -----------------------------
# Core logic
# -----------------------------


def recognize_gesture(landmarks):
    """Recognize a gesture from Mediapipe hand landmarks."""
    thumb_tip = landmarks[4]
    index_tip = landmarks[8]
    middle_tip = landmarks[12]
    ring_tip = landmarks[16]
    pinky_tip = landmarks[20]
    wrist = landmarks[0]

    def distance(p1, p2):
        return np.sqrt((p1.x - p2.x) ** 2 + (p1.y - p2.y) ** 2)

    # Distances and relative positions
    thumb_index_dist = distance(thumb_tip, index_tip)
    thumb_middle_dist = distance(thumb_tip, middle_tip)
    thumb_ring_dist = distance(thumb_tip, ring_tip)
    thumb_pinky_dist = distance(thumb_tip, pinky_tip)
    wrist_index_dist = distance(wrist, index_tip)
    wrist_thumb_dist = distance(wrist, thumb_tip)

    # Simple gesture rules (placeholder logic)
    if (
        thumb_index_dist > 0.2
        and thumb_middle_dist > 0.2
        and thumb_ring_dist > 0.2
        and thumb_pinky_dist > 0.2
    ):
        return "Hello"  # All fingers extended
    elif (
        thumb_index_dist < 0.1
        and thumb_middle_dist < 0.1
        and thumb_ring_dist < 0.1
        and thumb_pinky_dist < 0.1
    ):
        return "Goodbye"  # Fingers together, waving
    elif wrist_thumb_dist < wrist_index_dist and thumb_tip.y < wrist.y:
        return "Please"  # Flat hand, palm up
    elif wrist_thumb_dist < wrist_index_dist and thumb_tip.y > wrist.y:
        return "Thank You"  # Flat hand moving away from chin
    elif thumb_tip.x < index_tip.x:
        return "Yes"  # Fist with thumb up
    return None


def update_frame():
    """Grab a frame, run hand detection + gesture recognition, update GUI."""
    if cap is None or not cap.isOpened():
        return

    ok, frame = cap.read()
    if not ok:
        return

    # Convert BGR->RGB for Mediapipe
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    result = hands.process(rgb_frame)

    gesture = None
    if result.multi_hand_landmarks:
        for hand_landmarks in result.multi_hand_landmarks:
            mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)
            gesture = recognize_gesture(hand_landmarks.landmark)

    # Display frame in Tk
    img = Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
    imgtk = ImageTk.PhotoImage(image=img)

    video_label.imgtk = imgtk  # keep a reference!
    video_label.configure(image=imgtk)

    if gesture:
        gesture_label.config(text=f"Gesture: {gesture}")
        description_label.config(
            text=f"Description: {GESTURE_DESCRIPTIONS.get(gesture, '')}"
        )
        log_listbox.insert(tk.END, f"Gesture: {gesture}")
    else:
        gesture_label.config(text="Gesture: None")
        description_label.config(text="Description: None")

    # Schedule next frame
    video_label.after(10, update_frame)


# -----------------------------
# GUI actions
# -----------------------------


def start_video():
    global cap
    if cap is None or not cap.isOpened():
        cap = cv2.VideoCapture(0)
    update_frame()


def stop_video():
    global cap
    if cap is not None and cap.isOpened():
        cap.release()
    video_label.config(image="")
    video_label.imgtk = None


def clear_log():
    log_listbox.delete(0, tk.END)


def exit_app():
    stop_video()
    window.destroy()


# -----------------------------
# Tkinter UI
# -----------------------------

window = tk.Tk()
window.title("Makaton Gesture Recognition")

video_label = tk.Label(window)
video_label.pack()

gesture_label = tk.Label(window, text="Gesture: None", font=("Helvetica", 16))
gesture_label.pack()

description_label = tk.Label(window, text="Description: None", font=("Helvetica", 16))
description_label.pack()

toolbar = tk.Frame(window)
toolbar.pack(pady=5)

start_button = tk.Button(toolbar, text="Start Video", command=start_video)
start_button.pack(side=tk.LEFT, padx=10)

stop_button = tk.Button(toolbar, text="Stop Video", command=stop_video)
stop_button.pack(side=tk.LEFT, padx=10)

clear_log_button = tk.Button(toolbar, text="Clear Log", command=clear_log)
clear_log_button.pack(side=tk.LEFT, padx=10)

exit_button = tk.Button(toolbar, text="Exit", command=exit_app)
exit_button.pack(side=tk.LEFT, padx=10)

log_listbox = tk.Listbox(window, width=50, height=10)
log_listbox.pack(pady=10)

# -----------------------------
# Run
# -----------------------------

window.mainloop()

# Cleanup
if cap is not None and cap.isOpened():
    cap.release()
cv2.destroyAllWindows()
