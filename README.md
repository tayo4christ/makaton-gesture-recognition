![CI](https://github.com/tayo4christ/makaton-gesture-recognition/actions/workflows/ci.yml/badge.svg)

# Makaton Gesture Recognition Tool 🤖✋
[![Build](https://img.shields.io/badge/build-passing-brightgreen)](#)
[![License](https://img.shields.io/badge/license-MIT-blue)](#)
[![Coverage](https://img.shields.io/badge/coverage-80%25-green)](#)
[![Python](https://img.shields.io/badge/python-3.10%2B-yellow)](#)

---

## 🌍 Overview

This project provides a **real-time hand gesture recognition system** tailored to translate basic **Makaton gestures into English text**.
Built with computer vision and deep learning technologies, it enables **inclusive communication** for individuals with speech or language difficulties.

This innovation combines **computer vision and assistive AI** to make communication tools more inclusive and accessible for learners and individuals with speech challenges.

---

## 🔍 Problem It Solves

Many individuals who rely on Makaton for communication face barriers when interacting with non-Makaton users.
This tool bridges that gap by recognizing predefined hand gestures and translating them into English in real time, helping **Makaton and non-Makaton users** communicate more effectively.

---

## 👥 Intended Users

- Makaton users
- Educators and support staff working with individuals with communication difficulties
- Researchers and developers exploring gesture-based communication systems

---

## 🛠️ Technologies Used

- **Python**
- **OpenCV**
- **MediaPipe**
- **NumPy**
- **Tkinter** (for GUI)
- **Pillow** (for image display)

---

## ⚙️ System Architecture

Video Input ➜ Frame Extraction ➜ Hand Landmark Detection ➜ Gesture Classification ➜ English Translation ➜ Display on GUI

---

## 📥 Input / Output

**Input:**
Live webcam stream of hand gestures

**Output:**
Recognized Makaton gesture and corresponding English translation displayed on screen

---

## 💻 Usage Instructions

### 🧰 Prerequisites
Ensure you have Python 3.10 or higher installed, then install dependencies:

```bash
pip install opencv-python mediapipe numpy pillow

```

Running the Application
```bash
git clone https://github.com/tayo4christ/makaton-gesture-recognition.git
cd makaton-gesture-recognition
python makaton_recognition.py
```

Use your webcam to perform gestures. The GUI will display the detected gesture and its translation.
---

## ⚙️ Developer Setup

If you’d like to contribute or run the project in development mode, follow these steps:

### 1️⃣ Create and activate a virtual environment

```bash
python -m venv .venv
# On Windows
.\.venv\Scripts\Activate
# On macOS/Linux
source .venv/bin/activate
```

2️⃣ Install dependencies
```bash
pip install -r requirements.txt
```
3️⃣ Run pre-commit hooks locally (for formatting and linting)
```bash
pre-commit install
pre-commit run --all-files
```

4️⃣ Run tests
```bash
pytest -q
```
---

## ✅ Field Testing

The prototype was **tested with 8 students at Derby Cathedral School**, Derby, UK.
Feedback showed the interface was intuitive and translations were accurate for supported gestures.
This demonstrates **early-stage validation** and **real-world relevance** — essential for inclusive AI systems.

---

## 🧠 Recognized Gestures and Descriptions

| Gesture   | Description                                                          |
|------------|----------------------------------------------------------------------|
| Hello      | Open hand, palm facing forward, all fingers extended                 |
| Goodbye    | Open hand, palm facing forward, moving fingers as if waving          |
| Please     | Flat hand, palm facing up, moving in a small circular motion         |
| Thank You  | Flat hand, palm facing up, moving away from the chin                 |
| Yes        | Fist with thumb up                                                   |

---

## 📸 Screenshots / Demo

🎬 Demo video and screenshots available in the `media/` folder (add yours there).
Example:

![App Interface](media/demo-sample.png)

---

## 🧱 Project Structure

```text
makaton-gesture-recognition/
│
├── src/                  # Core source code
├── data/                 # Datasets
├── models/               # Model weights
├── notebooks/            # Research experiments
├── tests/                # Unit tests
├── media/                # Demo videos & screenshots
└── README.md             # Project documentation
```
---

## 🗺️ Roadmap

- [x] Initial prototype (gesture-to-text)
- [ ] Add dynamic Makaton gesture recognition (temporal analysis)
- [ ] Integrate English text-to-speech output
- [ ] Expand dataset beyond 10 core gestures
- [ ] Deploy a web demo using Streamlit or Gradio

---

## 🤝 Contributions

Contributions are welcome!
You can help by:

- Improving gesture detection accuracy
- Adding new signs
- Enhancing the GUI and accessibility features

Create a pull request or open an issue — let’s build accessible AI together 💪.

---

## 🧠 Author

**Omotayo Omoyemi**
MSc in Computer Science | Researcher in AI & Education

- **LinkedIn:** [https://www.linkedin.com/in/omotayo-emmanuel-omoyemi-mbcs-054484191/](https://www.linkedin.com/in/omotayo-emmanuel-omoyemi-mbcs-054484191/)
- **FreeCodeCamp Publications:** [https://www.freecodecamp.org/news/author/tayo4christ/](https://www.freecodecamp.org/news/author/tayo4christ/)
- **ACM Publication:** [https://dl.acm.org/doi/10.1145/3708635.3708647](https://dl.acm.org/doi/10.1145/3708635.3708647)

---

## 🧩 Version
**Current Release:** `v1.0.0`
Stable foundation with CI/CD, pre-commit hooks, Ruff linting, and auto-formatting.
Next milestone: implement gesture dataset expansion and text-to-speech.

---

## 📜 License

This project is open-source and available under the **MIT License**.
