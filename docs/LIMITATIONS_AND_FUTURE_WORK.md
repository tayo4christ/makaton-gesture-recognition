# 🧩 Limitations & Future Work
**Makaton Gesture Recognition Tool**

This document outlines the current limitations of the Makaton Gesture Recognition Tool and provides a forward-looking roadmap for future work. It is intended for researchers, developers, educators, and reviewers who want a transparent view of the system’s current capabilities and planned improvements.

---

## 🚧 1. Current Limitations

### 1.1 Rule-Based Gesture Recognition

The current system uses a **heuristic, rule-based recogniser**.

Limitations include:

- Sensitivity to hand shape variation
- Difficulty generalising across users
- Inaccuracy for ambiguous or overlapping gestures
- No adaptive learning from user behaviour

Rule-based recognition is reliable for prototypes and demos but not ideal for large-scale deployment.

---

### 1.2 Limited Gesture Set

The prototype currently recognises **five static gestures**:

- Hello
- Goodbye
- Please
- Thank You
- Yes

Limitations:

- No dynamic gestures (temporal gestures requiring motion analysis)
- No support for the full Makaton vocabulary
- No ability to customise or add user-defined gestures at runtime

---

### 1.3 Single-Hand Detection

Mediapipe supports multi-hand tracking, but the tool currently limits recognition to **single-hand gestures**.

Limitations:

- Cannot interpret two-handed Makaton signs
- No left-hand / right-hand distinction
- Cannot detect symmetrical or mirrored signs

---

### 1.4 Environmental Sensitivity

Performance can degrade under:

- Poor or uneven lighting
- Busy or cluttered backgrounds
- Strong shadows or glare
- Low-resolution webcams

The system assumes controlled school/classroom conditions.

---

### 1.5 No Temporal Gesture Modelling

Many Makaton signs are **dynamic**, requiring movement over time.

Current limitations:

- Processes frames independently
- No temporal sequence analysis
- No gesture transitions (start → hold → release)
- Cannot recognise motion-based gestures (e.g., “More”, “Finish”, “Stop”)

A future temporal model is needed.

---

### 1.6 No Personalisation or Adaptation

The current version does not:

- Learn from the user
- Adapt to different hand sizes or skin tones
- Allow calibrating for individual motor abilities
- Provide personalised accuracy profiles

Personalisation is critical for assistive technology.

---

### 1.7 Limited Error Feedback

The current UI provides:

- Detected gesture
- Description

But does not offer:

- Confidence scores
- Error explanations
- Alternative gesture suggestions
- Visual hand landmark debugging tools for advanced users

---

### 1.8 Desktop-Only

The tool currently depends on:

- Python
- Mediapipe
- OpenCV
- Tkinter

This limits deployment options — no:

- Mobile app
- Web app
- Browser-based client
- On-device edge model

---

## 🚀 2. Future Work & Planned Improvements

### 2.1 Machine Learning–Based Gesture Classifier

Next milestone:

- Train a deep learning model (e.g. CNN or MediaPipe Gesture Classifier)
- Replace rule-based logic with ML inference
- Provide probabilistic outputs
- Improve robustness across users and environments

This will significantly improve accuracy.

---

### 2.2 Dynamic Gesture Recognition

Introduce temporal models:

- Temporal CNN
- LSTM / GRU
- Transformer-based sequence models
- Optical flow for motion cues

This enables a wider set of Makaton signs and more natural interaction.

---

### 2.3 Expand the Gesture Dataset

Plan to build a high-quality dataset with:

- Multiple users
- Varied lighting
- Varied backgrounds
- Diverse hand shapes and skin tones
- Dynamic gestures
- Classroom and home environments

This will improve model generalisation.

---

### 2.4 Multi-Hand Support

Future versions will:

- Recognise two-handed gestures
- Distinguish left-hand vs right-hand roles
- Track hand interactions (e.g., touching chin, moving forward)

This is essential for fuller Makaton coverage.

---

### 2.5 Personalisation & Calibration

Introduce:

- Per-user calibration
- Adjustable sensitivity thresholds
- Adaptive gesture profiles
- A “learning mode” to train custom gestures

This aligns with inclusive design and accessibility goals.

---

### 2.6 Web & Mobile Deployment

Long-term work:

- WebAssembly (WASM) or WebGPU-based MediaPipe version
- Web-based interface (e.g. Streamlit / Gradio)
- Android / iOS mobile app
- On-device inference for privacy

This will increase impact and accessibility.

---

### 2.7 Real-Time Confidence Feedback

Add:

- Probability/confidence indicators
- Gesture confidence overlays
- Visual debugging tools
- Suggestions for clearer gestures

This improves usability in classroom environments.

---

### 2.8 Classroom Analytics Dashboard

Future goal:

- Log gesture frequency
- Track learner progress
- Generate learning analytics
- Provide periodic reports to teachers
- Measure engagement over time

This connects AI with educational outcomes.

---

## 🎯 3. Summary

This limitations and future work documentation shows that the Makaton Gesture Recognition Tool:

- Has a solid operational prototype
- Has been tested in real classrooms
- Has received external recognition
- Is actively evolving
- Has a clear technical roadmap
- Has well-understood limitations
- Has credible future directions

This transparency, roadmap, and research maturity support its use in academic, research, and innovation environments — including as evidence for Tech Nation.
