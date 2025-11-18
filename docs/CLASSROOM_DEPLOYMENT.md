# Classroom Deployment Guide
**Makaton Gesture Recognition Tool**

This guide provides practical instructions for deploying the Makaton Gesture Recognition Tool in real classroom environments. It is designed for teachers, support staff, and researchers who wish to use the system with learners for communication support or experimentation.

---

## 1. System Requirements

### Minimum Hardware
- Laptop or desktop computer (Windows/macOS/Linux)
- 4GB RAM (8GB recommended)
- Webcam (built-in or external)
- Basic lighting (classroom standard acceptable)

### Software Requirements
- Python 3.10+
- Dependencies installed using:
  ```bash
  pip install -r requirements.txt

---

## 2. Classroom Setup Recommendations

### Positioning the Camera
- Place the webcam at chest or head level.
- Ensure the student is 30–60 cm from the camera.
- Avoid extreme angles; keep the learner centered in frame.

### Lighting Guidelines
- Use even lighting — avoid strong shadows.
- Ensure hands are clearly visible and not merging with background colors.
- Natural daylight or classroom LED lighting is sufficient.

### Background
- Use a plain, uncluttered background when possible.
- Avoid patterned or highly reflective surfaces.

---

## 3. Teacher / Facilitator Checklist

### Before starting:
- Test the webcam feed
- Confirm gestures appear clearly
- Ensure students understand where to position hands
- Close any applications using the webcam
- Run the tool once to validate the gesture pipeline

### During use:
- Stay within the supported gesture set
- Ensure only one person’s hands are visible at a time
- Provide clear instructions to learners
- Monitor any misclassifications and record observations

### After use:
- Save any logs or notes
- Restart the app if performance decreases over time
- Turn off webcam when not in use

---

## 4. Best Practices for Accurate Recognition

### To achieve the highest accuracy:
- Perform gestures slowly and clearly.
- Hold the gesture for at least 1–2 seconds.
- Keep fingers separated for gestures like Hello or Goodbye.
- Avoid blocking the camera with sleeves or other objects.
- Use consistent lighting during the session.

---

## 5. Accessibility Considerations

- This tool is designed to support inclusive classroom environments.
- Students with limited hand mobility may need adapted gestures.
- Teachers can support by modelling gestures clearly before students attempt them.
- Always allow learners to engage at their own pace.
- Avoid pressuring learners if the tool does not recognise a gesture immediately.

---

## 6. Safety, Ethics & Responsible Use

This application:
- Does NOT store or upload video
- Does NOT send data to external servers
- Processes all hand landmarks locally on the device

However, please always follow:
- Classroom Data Safety Guidelines
- Do not record classroom video unless authorised.
- Do not store identifiable student footage.
- Ensure the webcam is turned off when the session ends.
- Follow your school’s safeguarding policies.

---

## 7. Classroom Testing Feedback Template

To help improve the tool, teachers may document:
- Classroom:
- Number of students:
- Gestures tested:
- Accuracy observed:
- Lighting conditions:
- Issues encountered:
- Student reactions:

Save this as a text note or attach to GitHub issues if appropriate.

---

## 8. Troubleshooting

Gesture not detected?
- Check lighting
- Move closer to the camera
- Keep hands within frame
- Restart the application
- Frequent misclassification?
- Ensure student is performing the exact supported gesture
- Avoid multiple hands in view
- Reduce background movement
- Webcam not working?
- Close Teams/Zoom/Chrome
- Restart the application
- Reconnect USB webcam if external

---

## 9. Support

For help or suggestions:
Read the full support guide: SUPPORT.md
Report issues:
https://github.com/tayo4christ/makaton-gesture-recognition/issues

Security concerns: SECURITY.md

---

## 10. Purpose of This Guide

This documentation supports the safe and effective use of the Makaton Gesture Recognition Tool in educational environments. It also demonstrates responsible deployment practices for inclusive assistive AI systems.
