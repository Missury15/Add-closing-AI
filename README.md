# 🚫 Ad-closing-AI

An AI-powered tool that automatically detects and closes ads using computer vision and automation. Powered by [YOLOv8](https://github.com/ultralytics/ultralytics), OpenCV, and Python's `pynput` library.

---

## 🎯 What It Does?

This project trains a custom object detection model to identify close buttons in advertisements and simulates a mouse click to close them - making your screen-time less annoying automatically!

---

## 🧠 How It Works?

### 1. **Training the Model**
Using the Ultralytics YOLOv8 model, we train it on a dataset of ad close buttons.

```python
from ultralytics import YOLO

# Load a YOLO model
model = YOLO('yolov8n.yaml')  # Choose a YOLOv8 model version

# Train on a labeled dataset
model.train(data='path/to/your/dataset.yaml', epochs=100)
