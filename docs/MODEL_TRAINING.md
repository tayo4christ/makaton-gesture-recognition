# Gesture Recognition Logic and Future Model Training
**Makaton Gesture Recognition Tool**

This document explains how gesture recognition currently works in this project and outlines how a future machine learning (ML) model can be integrated.

At the moment, the system uses a **rule-based recogniser** built on top of MediaPipe hand landmarks. No trained ML model is used yet. This is intentional: it keeps the system simple, interpretable, and easy to debug while the dataset is still small.

---

## 1. Current Recognition Pipeline (Rule-Based)

The current pipeline is:

1. Capture video frames from the webcam using OpenCV.
2. Detect hand landmarks with **MediaPipe Hands**.
3. Pass the landmarks into a **rule-based function**: `recognize_gesture(...)`.
4. Map the recognised gesture to an English label and description.
5. Display the video + recognised gesture in a Tkinter GUI.

The core function is:

```
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
```
This logic uses distances and relative positions of key landmarks (thumb tip, index tip, wrist, etc.) to decide which gesture is being performed.

---
## 2. Gesture Set and Descriptions

The recognised gestures are mapped to short human-readable descriptions:

```
GESTURE_DESCRIPTIONS = {
    "Hello": "Open hand, palm facing forward, all fingers extended.",
    "Goodbye": "Open hand, palm facing forward, moving fingers as if waving.",
    "Please": "Flat hand, palm facing up, moving in a small circular motion.",
    "Thank You": "Flat hand, palm facing up, moving away from the chin.",
    "Yes": "Fist with thumb up.",
}
```
This keeps the tool explainable for:

- educators,
- learners, and
- researchers evaluating the system.

---

## 3. Why Rule-Based First (and Not a Model Yet)

The project currently uses rules instead of a trained ML model because:

- There is no large, labelled Makaton gesture dataset yet.
- Rule-based logic is transparent and easy to debug.
- It allows quick iteration while testing in classrooms.
- It works well enough for a small set of core gestures.
This design also makes it easier to collect data and refine rules before committing to a learned model.

---

## 4. How a Future ML Model Will Fit In

Although there is no trained ML model in the repository yet, the structure is designed so that a model can be plugged in later.

A future ML-based pipeline would look like:

- Capture video frames and detect landmarks (same as now).
- Convert landmarks to a feature vector.
- Pass the vector into a trained classifier (e.g. neural network, SVM, random forest).
- Get predicted gesture label ("Hello", "Goodbye", etc.).
- Use the same GUI and descriptions to display the result.

Conceptually, this can be represented as:
Frame → MediaPipe landmarks → Feature vector → Trained model → Gesture label

The current recognize_gesture(...) can later be replaced or extended with a model-based recogniser.

## 5. Feature Representation for a Model (Design Plan)

When a model is introduced, each frame (or short sequence) will be converted into a numerical feature vector, for example:

- Normalised (x, y) coordinates of each landmark
- Distances between key fingertips and the wrist
- Angles between fingers or finger segments

```
def landmarks_to_features(landmarks):
    # Flatten landmark coordinates into a feature vector
    features = []
    for lm in landmarks:
        features.append(lm.x)
        features.append(lm.y)
    return np.array(features, dtype=np.float32)
```
These feature vectors will be used as inputs for training a classifier.

---
## 6. Future Training Workflow (Planned)

Once a dataset exists (see DATASET_GUIDE.md), a basic training loop might look like:

- Load landmark-based feature vectors and labels ("Hello", "Please", etc.).
- Split into train/validation sets.
- Train a classifier (e.g. scikit-learn, PyTorch, TensorFlow).
- Evaluate accuracy and confusion matrix.
- Export the trained model to disk (e.g. model.joblib or model.onnx).
- Load the model inside the app and replace the rule-based function.

Pseudo-code example:
```
# PSEUDO-CODE: illustrates the plan, not implemented yet

from sklearn.ensemble import RandomForestClassifier
import joblib

X_train, y_train = load_features_and_labels("data/")  # planned
clf = RandomForestClassifier(n_estimators=200, random_state=42)
clf.fit(X_train, y_train)

joblib.dump(clf, "models/gesture_classifier.joblib")

```
At runtime, the app would:

```
# PSEUDO-CODE:
clf = joblib.load("models/gesture_classifier.joblib")

def recognize_gesture_model(landmarks):
    features = landmarks_to_features(landmarks)
    prediction = clf.predict([features])[0]
    return prediction

```
---
## 7. Transition Strategy: Rules → Model

The migration plan is:

1. Phase 1 (current): Pure rule-based recogniser
2. Phase 2: Hybrid approach
- Try the model first
- Fall back to rules if confidence is low
3. Phase 3: Fully model-based, with rules optionally kept for debugging or safety checks
This staged approach ensures:
- No sudden breakage for users
- Easy comparison between rule-based and model-based performance
- Clear path for research and evaluation
---
## 8. Summary

- The current project uses a rule-based recogniser, not a trained model.
- MediaPipe provides hand landmarks; distances and relative positions are used to classify gestures.
- This approach is simple, interpretable, and suitable for early-stage classroom testing.
- MODEL_TRAINING.md also documents a future design for training and integrating an ML model, once a suitable dataset is available.

As the dataset grows and more gestures are added, this document will guide the implementation of a full model training pipeline.
