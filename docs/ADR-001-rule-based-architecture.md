# Architecture Decision Record (ADR)
**Project:** Makaton Gesture Recognition Tool
**ADR-001:** Choice of Rule-Based Gesture Recognition (Phase 1)
**Status:** Accepted
**Date:** 2025-02-10

---

## 1. Context
The system needs a reliable method of recognising Makaton hand gestures in real time using a webcam.
Two main approaches were considered:

1. **Rule-Based Recognition** (geometric thresholds using MediaPipe landmarks)
2. **Machine Learning Model** (trained classifier using a labelled dataset)

The current project is used in schools, demonstrated publicly, and evaluated in real-world settings, so early versions must be:

- transparent
- explainable
- safe for classroom use
- runnable on basic laptops
- stable without large datasets

---

## 2. Decision
We selected a **rule-based gesture recognition engine** for Phase 1 of the project.

This includes:

- Using MediaPipe to extract hand landmarks
- Applying geometric rules (distances, angles, and relative positions)
- Mapping gestures to fixed descriptions
- Ensuring deterministic outputs for testing and auditing

---

## 3. Rationale
The rule-based approach was chosen because:

### ✔ Explainability
Educators and researchers can understand why a gesture was recognised.

### ✔ Low computational cost
Runs smoothly on non-GPU machines (e.g., school laptops).

### ✔ No training data required
A fully labelled Makaton dataset does not yet exist.

### ✔ Enables safe field testing
Consistent behaviour is essential for classroom deployment.

### ✔ Provides a foundation for future ML integration
The architecture allows the rule-based engine to be replaced later without modifying the UI or video pipeline.

---

## 4. Alternatives Considered
### **A. Machine Learning Classifier (Rejected for Phase 1)**
Reasons:
- Requires collecting 1,000+ labelled gesture samples
- More complex debugging for early prototypes
- Risks unpredictable behaviour in real-time demos
- Harder to audit or explain to school partners

---

## 5. Consequences
### **Positive**
- Faster development and deployment
- Strong transparency and auditability
- Easy to extend gesture rules
- Suitable for education and research environments

### **Negative**
- Limited scalability for complex gestures
- Lower accuracy for dynamic gestures
- Requires ML upgrade in future phases

---

## 6. Future Plan
Phase 2 will introduce an ML-based gesture model:

- Landmark → feature vector → trained classifier
- Hybrid mode (Model + Rule fallback)
- Eventual migration to full ML once dataset is ready

---

## 7. Summary
This ADR documents the foundational architectural decision to use a rule-based engine in Phase 1, ensuring a stable, interpretable, and deployable system while maintaining a clear path for ML integration in future releases.
