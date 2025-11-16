![CI](https://github.com/tayo4christ/makaton-gesture-recognition/actions/workflows/ci.yml/badge.svg)

<p align="center">
  <img src="Media/banner.png" alt="Makaton Gesture Recognition Tool Banner" width="100%">
</p>

[![Build](https://img.shields.io/badge/build-passing-brightgreen)](#)
[![License](https://img.shields.io/badge/license-MIT-blue)](#)
[![Coverage](https://img.shields.io/badge/coverage-80%25-green)](#)
[![Python](https://img.shields.io/badge/python-3.10%2B-yellow)](#)

---

[![Status](https://img.shields.io/badge/status-active-success.svg)](#)
[![Research](https://img.shields.io/badge/research-AI%20%26%20Education-blue.svg)](#)
[![Made with Python](https://img.shields.io/badge/made%20with-Python%203.10+-yellow.svg)](#)
[![Maintained](https://img.shields.io/badge/maintained-yes-green.svg)](#)
[![Contributions welcome](https://img.shields.io/badge/contributions-welcome-brightgreen.svg)](#)

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

Before contributing, please read our [CONTRIBUTING.md](CONTRIBUTING.md) guide for details on:
- Project setup and environment
- Code style and commit conventions
- How to open pull requests or report issues

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

## 🌐 Community & Code of Conduct

We’re committed to fostering an open, welcoming, and harassment-free community for everyone.
Please read our [Code of Conduct](CODE_OF_CONDUCT.md) before contributing.

[![Contributor Covenant](https://img.shields.io/badge/Contributor%20Covenant-2.1-4baaaa.svg)](https://www.contributor-covenant.org/)

---

## 🔍 Project Insights

This project is part of ongoing research on **AI-assisted communication systems**, focusing on translating Makaton gestures into English.
It explores **computer vision**, **gesture recognition**, and **assistive technology for inclusion**.

Future research directions include:
- Integrating speech synthesis for full gesture-to-speech communication
- Improving temporal recognition of dynamic gestures
- Expanding datasets for better generalization
- Exploring multimodal inputs (e.g., face expressions, context awareness)

---

**Research Focus:** Inclusive AI • Assistive Technology • Computer Vision • NLP Integration

---

## 📚 Citations & References

If you reference or build upon this project in academic or research work, please cite:

> S. Karkalas, Omoyemi O. (2024). *Designing a tool that automatically translate Makaton signs from Live video streams into English.*
> In Proceedings of the 13th International Conference on Software and Information Engineering (ICSIE 2024).
> DOI: [10.1145/3708635.3708647](https://dl.acm.org/doi/10.1145/3708635.3708647)

This repository also draws inspiration from:
- Google Mediapipe Hand Tracking documentation
- OpenCV real-time video analysis guides
- Python Tkinter GUI frameworks for accessibility tools

---

## 💬 Support & Help

If you need help using the Makaton Gesture Recognition Tool or want to report a problem, please:

- First read the [SUPPORT.md](SUPPORT.md) guide for common issues and FAQs.
- Open a [GitHub issue](https://github.com/tayo4christ/makaton-gesture-recognition/issues) for bug reports and feature requests.
- For security-related concerns, follow the process described in [SECURITY.md](SECURITY.md).

> Note: This tool is **not** a replacement for official Makaton training.
> For learning or teaching Makaton itself, please refer to official Makaton training providers and resources in your region.
---

## 🙏 Acknowledgements

Special thanks to the open-source community projects and mentors who inspired this work:
- **MediaPipe** by Google for providing accessible hand-tracking tools
- **OpenCV** community for continuous innovation in computer vision
- **Dr. Sokratis Karkalas** for research guidance and collaboration during ICSIE 2024
- All educators and students who provided early feedback during prototype testing

---

## 📜 License

This project is open-source and available under the **MIT License**.
