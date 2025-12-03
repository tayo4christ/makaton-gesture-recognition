# 📘 User Guide
**Makaton Gesture Recognition Tool**
*Inclusive AI for Accessible Communication*

---

## ⭐ 1. Introduction

The Makaton Gesture Recognition Tool enables real-time translation of basic Makaton hand gestures into English text using computer vision and assistive AI.

This guide provides everything you need to install, run, and use the tool effectively — whether you are:

- a **teacher**
- a **learner**
- a **researcher**
- or a **developer contributing to the project**

The tool is designed to be **simple, safe, and accessible**, requiring only a webcam and a standard laptop.

---

## ⭐ 2. System Requirements

### ✔ Hardware
- Laptop or desktop computer
- 4GB RAM minimum (8GB recommended)
- Built-in or USB webcam
- Standard indoor lighting

### ✔ Supported Operating Systems
- Windows
- macOS
- Linux

### ✔ Software Requirements
- Python **3.10+**
- Dependencies listed in `requirements.txt`

---

## ⭐ 3. Installation

### 3.1 Clone the Repository
```
git clone https://github.com/tayo4christ/makaton-gesture-recognition.git
cd makaton-gesture-recognition
```
---

### 3.2 Create and Activate a Virtual Environment
```
python -m venv .venv
.\.venv\Scripts\activate

```
macOS/Linux:
```
python3 -m venv .venv
source .venv/bin/activate
```

3.3 Install Dependencies
```
pip install -r requirements.txt
```
---

## 4. Running the Application

From the project root directory:
```
python makaton_gesture_recognition.py
```
When the interface opens:

Click Start Video

- Position your hand clearly in front of the webcam
- Perform one of the supported gestures
- The detected gesture and its English meaning will appear on screen
- To stop the camera, click Stop Video.
- To close the app, click Exit.

## 5. Supported Gestures

The tool currently supports the core gestures:
| Gesture       | Description                               |
| ------------- | ----------------------------------------- |
| **Hello**     | Open hand, palm facing forward            |
| **Goodbye**   | Waving hand                               |
| **Please**    | Flat hand, palm up, small circular motion |
| **Thank You** | Flat hand moving away from chin           |
| **Yes**       | Fist with thumb up                        |

More gestures will be added in future versions.

---

## 6. How to Perform Gestures Clearly

For best accuracy:

- Keep your hand fully inside the camera frame
- Perform gestures slowly and clearly
- Avoid covering your hand with sleeves or objects
- Ensure only one person's hand is visible
- Use good lighting — hands should be easy to see

---

## 7. Troubleshooting

❗ Webcam Not Detected

- Close Zoom, Teams, or any software using the camera
- Restart the app
- Try changing the camera index in the config file (future feature)

❗ Gesture Not Recognised

- Ensure your hand is centered in the frame
- Move slightly closer to the webcam
- Improve lighting
- Hold the gesture for at least 1–2 seconds

❗ App Feels Slow

- Close unnecessary background applications
- Reduce lighting fluctuations
- Check CPU usage
- Consider disabling HD webcam modes

---

8. Data Safety & Privacy

This tool is designed with safety in mind:

- No images or video are recorded
- No data is uploaded or sent to any server
- All processing happens locally on your device
- No biometric data is stored

For classroom use, refer to the Classroom Deployment Guide.

---

## 9. Accessibility Notes

The tool is designed to support:

- learners with speech or language difficulties
- children using Makaton in special education settings
- individuals who benefit from visual communication aids

Teachers can support students by:

- demonstrating gestures clearly
- allowing learners to take their time
- ensuring a comfortable interaction environment
- adapting gestures when needed based on physical ability

---

## 10. Frequently Asked Questions (FAQ)

- Q: Does the app learn from new gestures?
No — the current version uses rule-based recognition.
A future ML model will be added (see MODEL_TRAINING.md).

- Q: Does the app store video or images?
No. Everything is processed in real time and discarded immediately.

- Q: Can I add new gestures?
Yes — see the developer documentation in the docs/ folder.

- Q: Can this run on a Raspberry Pi?
Potentially, with some optimisation and lower resolution settings.

---

## 11. Developer Features

This tool includes:

- Logging (logs/)
- Config system (config.yaml)
- Benchmarking (benchmark.py)
- Unit tests (tests/)
- Dataset guide (DATASET_GUIDE.md)
- Classroom deployment documentation
- Model training roadmap

Developers can run tests using:
```
pytest -q
```
---

## 12. Contact & Support

For issues or suggestions, visit:

👉 GitHub Issues:
https://github.com/tayo4christ/makaton-gesture-recognition/issues

For additional guidance, see:

SUPPORT.md
SECURITY.md

---

13. Summary

This User Guide helps:

- teachers to use the tool in classrooms
- learners to interact confidently
- researchers to evaluate its performance
- developers to understand installation and operation

The Makaton Gesture Recognition Tool continues to evolve into a robust assistive AI platform.
