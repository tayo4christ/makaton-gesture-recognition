# System Architecture
**Makaton Gesture Recognition Tool**

## Purpose of This Document
This architecture document describes the internal structure, data flow, and component interactions of the Makaton Gesture Recognition Tool.
It is intended for technical reviewers, collaborators, and future contributors who need to understand the design principles, dependencies, and extensibility of the system.

## Overview
This document provides a technical deep dive into the architecture of the Makaton Gesture Recognition Tool.
It describes the system components, data flow, gesture recognition pipeline, and future machine learning integration.

---

## 1. High-Level Overview

The application is composed of three major modules:

1. **Video Input & Frame Processing**
   - Captures live webcam frames using OpenCV.
   - Converts frames to RGB for MediaPipe.

2. **Hand Landmark Detection & Gesture Recognition**
   - MediaPipe extracts 21 hand landmarks per frame.
   - A custom rule-based recogniser classifies gestures using geometric relationships.

3. **Graphical User Interface (GUI)**
   - Displays video stream, recognised gesture, description, and logs events using Tkinter.

### System Modules and Boundaries
The system is structured into well-defined layers:

- **Input Layer** – webcam capture and frame preprocessing
- **Perception Layer** – MediaPipe-based landmark extraction
- **Recognition Layer** – rule-based gesture classification
- **Presentation Layer** – UI rendering and live feedback via Tkinter
- **Support Services** – configuration loading, logging, benchmarking, and tests

This modular architecture ensures the recognition layer can evolve independently (e.g., move to ML models) without redesigning the rest of the system.

---

## 2. Data Flow Diagram

              ┌──────────────────┐
              │     Webcam       │
              │  (Live Video)    │
              └───────▲──────────┘
                      │ Frames
                      │
              ┌───────┴──────────┐
              │    OpenCV         │
              │ Frame Capture      │
              └───────▲──────────┘
                      │ RGB Frame
                      │
              ┌───────┴──────────┐
              │   MediaPipe       │
              │ Hand Landmarks    │
              └───────▲──────────┘
                      │ 21 Landmark Points
                      │
              ┌───────┴──────────┐
              │ Rule-Based        │
              │ Gesture Classifier│
              └───────▲──────────┘
                      │ Gesture Label
                      │ (Hello / Yes / Please)
                      │
              ┌───────┴──────────┐
              │     Tkinter GUI   │
              │ Video + Label +   │
              │ Description + Log │
              └───────────────────┘

### Mermaid Architecture Diagram (Rendered on GitHub)

```
flowchart LR
    A[Webcam (Live Video)] --> B[OpenCV Frame Capture]
    B --> C[MediaPipe Hands (21 Landmarks)]
    C --> D[Rule-Based Gesture Recogniser]
    D --> E[Gesture Label + Description]
    E --> F[Tkinter GUI (Real-Time Display)]
    D --> G[Logging System]
    C --> G
    B --> G
```
---
## 3. Component Breakdown

### 3.1 Video Processing (OpenCV)

- Captures frames from webcam (`cv2.VideoCapture(0)`).
- Converts BGR → RGB for MediaPipe:
  ```python
  rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

  ```
Sends frames to the next stage.

### 3.2 Hand Landmark Detection (MediaPipe Hands)

MediaPipe outputs:

- 21 (x, y, z) hand landmarks
- Handedness (left/right)
- Gesture-agnostic finger and palm positions

Landmarks are structured as:
```
[WRIST, THUMB_CMC, THUMB_MCP, THUMB_IP, THUMB_TIP, INDEX_MCP, INDEX_PIP, ... , PINKY_TIP]
```
### 3.3 Gesture Recognition Engine (Rule-Based)

The recogniser uses:

- Euclidean distances between key fingertips
- Relative position of thumb tip to wrist
- Relative heights of fingers
- Finger openness/closedness patterns

Example:
```
if thumb_index_dist > 0.2 and all_fingers_extended:
    return "Hello"
```
This approach is:

- Lightweight
- Deterministic
- Transparent (easy to debug)
- Suitable for early-stage prototypes and classroom testing

### 3.4 Rationale for Rule-Based Recognition (Current Phase)

The rule-based gesture recogniser is used in the current version because:

- It provides full explainability, which is important in educational settings
- It allows deterministic debugging of gesture rules
- It is lightweight and runs efficiently in real time
- It avoids dependency on a large dataset, which is still being collected

This approach forms a stable foundation while enabling a smooth transition towards a trained ML model.

---

## 4. Future Machine Learning Integration

The architecture anticipates a future ML classifier:
```
Landmarks → Feature Vector → Classifier (ML Model) → Gesture Label
```
Where the model could be:
- Random Forest
- SVM
- Shallow neural network
- LSTM/Temporal model (for dynamic gestures)

This hybrid design ensures:
- Current rule-based engine remains the fallback
- A trained model can be added without rewriting the GUI

---

## 5. ML Integration Compatibility

The recognition layer is intentionally isolated so that future trained models
(e.g., ONNX, scikit-learn, PyTorch) can replace the rule-based engine
without requiring changes to:

- the GUI
- the webcam pipeline
- MediaPipe landmark extraction
- the logging system
- configuration files

This demonstrates forward compatibility and ensures a seamless upgrade path.

---

## 6. GUI Architecture (Tkinter)

The GUI includes:

- Video display widget
- Gesture label (Gesture: Hello)
- Description label
- Log listbox (records every recognised gesture)

Toolbar with buttons:
- Start Video
- Stop Video
- Clear Log
- Exit App

All updates are event-driven:
```
video_label.after(10, update_frame)

```
This ensures non-blocking UI performance during video processing.

---

## 7. Error Handling & Fail-Safe Logic

- If no hand is detected → show “Gesture: None”
- If camera stops → GUI clears frame
- If wrong data → skip frame gracefully
- If MediaPipe fails → system falls back safely without crashing

---

## 8. Cross-Cutting Concerns

Several system-wide services operate independently of the gesture recognition logic:

- Logging – structured logs used for debugging, performance evaluation, and system monitoring
- Configuration Management – centralised via config.yaml for thresholds, camera index, and UI timing
- Benchmarking Tools – measure FPS and latency for optimisation
Error Handling – ensures graceful recovery if webcam frames fail or MediaPipe encounters invalid input

These concerns are intentionally decoupled from business logic to improve maintainability.

---

## 9. Performance Considerations

- Real-time processing at 720p
- Landmark extraction is the heaviest step
- Rule-based classification runs in microseconds
- Tkinter refreshes at ~100 FPS internally
- Memory usage stays minimal (<200MB in most cases)

---

## 10. Architectural Constraints

The current design operates under the following constraints:

- MediaPipe Hands runs on CPU (no GPU acceleration in Python)
- Tkinter is single-threaded and requires non-blocking UI updates
- Real-time performance limits the use of heavy ML models in early prototypes
- All processing must occur locally to comply with safeguarding requirements in classrooms

---

## 11. Future Improvements

- Replace rule-based logic with trained model
- Add gesture confidence scores
- Add multi-hand support
- Implement temporal modelling for dynamic gestures
- Export results to CSV logs
- Move to PyQt or web GUI later

---

## 12. Summary

This architecture ensures:

- Real-time gesture recognition
- Stable performance on consumer hardware
- Clean modular design
- Easy future upgrade to ML
- Clear separation between UI, recognition logic, and video pipeline

This document serves as a technical reference for contributors, reviewers, and grant or endorsement evaluators assessing the engineering depth of the project.
