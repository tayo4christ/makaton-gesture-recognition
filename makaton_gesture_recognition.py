import cv2
import mediapipe as mp
import numpy as np
from tkinter import *
from PIL import Image, ImageTk

# Initialize Mediapipe hands module
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(max_num_hands=1)
mp_drawing = mp.solutions.drawing_utils

# Define the gesture descriptions
GESTURE_DESCRIPTIONS = {
    'Hello': 'Open hand, palm facing forward, all fingers extended.',
    'Goodbye': 'Open hand, palm facing forward, moving fingers as if waving.',
    'Please': 'Flat hand, palm facing up, moving in a small circular motion.',
    'Thank You': 'Flat hand, palm facing up, moving away from the chin.',
    'Yes': 'Fist with thumb up.'
}

# Function to recognize gestures based on hand landmarks
def recognize_gesture(landmarks):
    thumb_tip = landmarks[4]
    index_tip = landmarks[8]
    middle_tip = landmarks[12]
    ring_tip = landmarks[16]
    pinky_tip = landmarks[20]
    wrist = landmarks[0]

    # Distances between landmarks
    def distance(point1, point2):
        return np.sqrt((point1.x - point2.x)**2 + (point1.y - point2.y)**2)

    # Calculate distances and relative positions
    thumb_index_dist = distance(thumb_tip, index_tip)
    thumb_middle_dist = distance(thumb_tip, middle_tip)
    thumb_ring_dist = distance(thumb_tip, ring_tip)
    thumb_pinky_dist = distance(thumb_tip, pinky_tip)
    wrist_index_dist = distance(wrist, index_tip)
    wrist_thumb_dist = distance(wrist, thumb_tip)

    # Gesture recognition logic
    if thumb_index_dist > 0.2 and thumb_middle_dist > 0.2 and thumb_ring_dist > 0.2 and thumb_pinky_dist > 0.2:
        return 'Hello'  # All fingers extended
    elif thumb_index_dist < 0.1 and thumb_middle_dist < 0.1 and thumb_ring_dist < 0.1 and thumb_pinky_dist < 0.1:
        return 'Goodbye'  # Fingers together, waving
    elif wrist_thumb_dist < wrist_index_dist and thumb_tip.y < wrist.y:
        return 'Please'  # Flat hand, palm up
    elif wrist_thumb_dist < wrist_index_dist and thumb_tip.y > wrist.y:
        return 'Thank You'  # Flat hand moving away from chin
    elif thumb_tip.x < index_tip.x:
        return 'Yes'  # Fist with thumb up
    return None

# Function to update the video feed in the GUI
def update_frame():
    if not cap.isOpened():
        return

    ret, frame = cap.read()
    if not ret:
        return

    # Convert the frame color to RGB
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Process the frame and find hands
    result = hands.process(rgb_frame)

    gesture = None
    # Draw hand landmarks and recognize gestures
    if result.multi_hand_landmarks:
        for hand_landmarks in result.multi_hand_landmarks:
            mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)
            gesture = recognize_gesture(hand_landmarks.landmark)

    # Convert the frame to an image for tkinter
    img = Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
    imgtk = ImageTk.PhotoImage(image=img)

    # Update the GUI elements
    video_label.imgtk = imgtk
    video_label.configure(image=imgtk)
    if gesture:
        gesture_label.config(text=f"Gesture: {gesture}")
        description_label.config(text=f"Description: {GESTURE_DESCRIPTIONS.get(gesture, '')}")
        log_listbox.insert(END, f"Gesture: {gesture}")
    else:
        gesture_label.config(text="Gesture: None")
        description_label.config(text="Description: None")

    video_label.after(10, update_frame)

# Function to start video capture
def start_video():
    global cap
    cap = cv2.VideoCapture(0)
    update_frame()

# Function to stop video capture
def stop_video():
    global cap
    cap.release()
    video_label.config(image='')

# Function to clear the history log
def clear_log():
    log_listbox.delete(0, END)

# Function to exit the application
def exit_app():
    stop_video()
    window.quit()

# Initialize the GUI window
window = Tk()
window.title("Makaton Gesture Recognition")

# Create GUI elements
video_label = Label(window)
video_label.pack()

gesture_label = Label(window, text="Gesture: None", font=("Helvetica", 16))
gesture_label.pack()

description_label = Label(window, text="Description: None", font=("Helvetica", 16))
description_label.pack()

start_button = Button(window, text="Start Video", command=start_video)
start_button.pack(side=LEFT, padx=10)

stop_button = Button(window, text="Stop Video", command=stop_video)
stop_button.pack(side=LEFT, padx=10)

clear_log_button = Button(window, text="Clear Log", command=clear_log)
clear_log_button.pack(side=LEFT, padx=10)

exit_button = Button(window, text="Exit", command=exit_app)
exit_button.pack(side=LEFT, padx=10)

log_listbox = Listbox(window, width=50, height=10)
log_listbox.pack(pady=10)

# Run the GUI loop
window.mainloop()

# Release the video capture and close all windows
if cap.isOpened():
    cap.release()
cv2.destroyAllWindows()
