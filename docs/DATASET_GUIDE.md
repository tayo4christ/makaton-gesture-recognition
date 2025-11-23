# Dataset Guide
**Makaton Gesture Recognition Tool**

This guide explains how to collect, organise, and extend the dataset used for training the gesture recognition model.
It is intended for researchers, contributors, and developers who wish to improve classification accuracy, add new gestures, or reproduce experiments.

---

## 📁 1. Dataset Structure

The recommended dataset folder layout is:

data/
│
├── hello/
│ ├── frame_001.jpg
│ ├── frame_002.jpg
│ └── ...
│
├── goodbye/
│ ├── frame_001.jpg
│ ├── frame_002.jpg
│ └── ...
│
├── please/
├── thank_you/
└── yes/


Each folder contains **images or extracted frames** of a single gesture.

### Naming conventions:
- Use lowercase gesture names
- Use consistent naming: `frame_###.jpg`
- Use separate folders for **each gesture class**

---

## 🎥 2. How to Capture New Gesture Data

### Option A — Using a Webcam
You can record gesture videos using:

- Your laptop webcam
- An external USB webcam
- A mobile phone (then transfer to your PC)

**Steps:**

1. Record each gesture for **5–10 seconds**
2. Ensure hands stay within the frame
3. Use good lighting
4. Perform the gesture **slowly and clearly**
5. Save the video as `.mp4` or `.mov`

### Option B — Using the Tool's Built-In Recorder (future feature)
A recorder will be included in a future version to streamline data capture.

---

## 🖼️ 3. Extracting Frames From Videos

Use OpenCV to extract frames from a video:

```python
import cv2
import os

def extract_frames(video_path, output_folder):
    os.makedirs(output_folder, exist_ok=True)
    cap = cv2.VideoCapture(video_path)

    frame_count = 0
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        file_path = os.path.join(output_folder, f"frame_{frame_count:04d}.jpg")
        cv2.imwrite(file_path, frame)
        frame_count += 1

    cap.release()

extract_frames("hello.mp4", "data/hello")

This creates frame_0000.jpg, frame_0001.jpg, etc.



🧹 4. Clean and Preprocess the Dataset

Before training:
- Remove blurry frames
- Remove frames where the gesture is not fully visible
- Ensure consistent lighting and backgrounds
- Make sure only one person’s hands are in the video
- Crop or resize images (optional)

 Standard preprocessing:
- Resize all frames to 224×224
- Normalise pixel values
- Convert to RGB if needed

🧠 5. Gesture Categories (Current Supported Set)

The tool currently supports:

| Gesture   | Description                            |
| --------- | -------------------------------------- |
| Hello     | Open hand, palm forward                |
| Goodbye   | Waving hand                            |
| Please    | Flat hand making small circular motion |
| Thank You | Hand moving forward from the chin      |
| Yes       | Fist with thumb up                     |

When adding new gestures, ensure:

- The sign is consistent
- Movements are easy for the model to distinguish
- Enough samples (recommended 200–500 frames per gesture)

📈 6. Recommended Dataset Size

For each gesture:

- Minimum: 150 images
- Good: 300–500 images
- Best: 1,000+ images

Variety improves performance:
- Different lighting
- Different backgrounds
- Different people
- Different hand shapes and skin tones

⚖️ 7. Data Ethics & Permissions

This tool processes gestures, not identity.
Still, responsible data collection is essential.

You MUST ensure:
- Do not record faces intentionally
- Avoid capturing background bystanders
- Students or participants must have permission
- Follow school or institutional safeguarding policies
- Delete raw videos after extracting frames unless required
- All processing is local — no data is uploaded or transmitted.

🏗️ 8. Adding a New Gesture Class

To add a new gesture:
1. Create a folder in data/:  data/new_gesture_name/
2. Collect and extract frames
3. Add the new folder to the training script
4. Retrain the gesture classification model
5. Update gesture mapping in the application GUI
6. Add description to documentation

🧪 9. Evaluating Dataset Quality

Check for:
- Balanced classes (avoid class imbalance)
- Clear visibility of hands
- Consistent gesture performance
- No overlapping gestures
- No mixed frames (e.g., accidental gestures)

Use a simple test script to preview frames:
import cv2
cv2.imshow("example", cv2.imread("data/hello/frame_0001.jpg"))
cv2.waitKey(0)

🛠️ 10. Troubleshooting
Dataset too small?
→ Collect more videos with varied backgrounds.

Model misclassifies gestures?
→ Check for inconsistent or noisy frames.

Poor performance with real users?
→ Lighting or camera position may be the issue.

🔗 11. Related Documentation

MODEL_TRAINING.md (recommended next documentation)
CLASSROOM_DEPLOYMENT.md
README.md
SUPPORT.md
SECURITY.md

📜 12. Purpose of This Guide

This guide supports transparent, responsible dataset creation for gesture recognition research and development.
It also helps ensure reproducible experiments, better model performance, and safe deployment in educational contexts.
