from ultralytics import YOLO

# Load a YOLO model
model = YOLO('yolov8n.yaml')  # You can choose different YOLO versions

# Train the model
model.train(data='path/to/your/dataset.yaml', epochs=100)
