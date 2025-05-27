# Makaton Gesture Recognition Tool

This project provides a real-time hand gesture recognition system tailored to translate basic Makaton gestures into English text. Built with computer vision and deep learning technologies, the system enables accessibility and communication support for Makaton users.

---

## 🔍 Problem It Solves

Many individuals who rely on Makaton for communication face barriers in interacting with non-Makaton users. This tool bridges that gap by recognizing predefined hand gestures and translating them into English in real time.

---

## 👥 Intended Users

- Makaton users
- Educators and support staff working with individuals with communication difficulties
- Developers exploring gesture-based communication systems

---

## 🛠️ Technologies Used

- Python
- OpenCV
- MediaPipe
- NumPy
- Tkinter (for GUI)
- Pillow (for image display)

---

## 📥 Input / Output

- **Input**: Live video stream of hand gestures
- **Output**: Recognized Makaton gesture and its corresponding English translation shown on-screen

---

## 💻 Usage Instructions

### Prerequisites

Ensure you have Python 3 installed and install the following dependencies:

```bash
pip install opencv-python mediapipe numpy pillow
```

### Running the Application

1. Clone this repository
2. Run the Python script using:

```bash
python makaton_recognition.py
```

3. Use your webcam to perform gestures. The GUI will display the detected gesture and its description.

---

## ✅ Tested Users

The application has been tested with 8 students at Derby Cathedral School. Feedback indicated that the interface was intuitive and the translation accurate for supported gestures.

---

## 📸 Screenshots / Demo

> 📽️ Demo video and screenshots available in the `media/` folder (you can add yours there).

---

## 🧠 Recognized Gestures and Descriptions

| Gesture     | Description                                                         |
|-------------|----------------------------------------------------------------------|
| Hello       | Open hand, palm facing forward, all fingers extended                |
| Goodbye     | Open hand, palm facing forward, moving fingers as if waving         |
| Please      | Flat hand, palm facing up, moving in a small circular motion        |
| Thank You   | Flat hand, palm facing up, moving away from the chin                |
| Yes         | Fist with thumb up                                                  |

---

## 📃 License

This project is open-source and available under the MIT License.

---

## 🙌 Contributions

You're welcome to contribute by improving gesture detection, adding new signs, or enhancing the UI.

