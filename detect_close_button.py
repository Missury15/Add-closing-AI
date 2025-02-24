import cv2
from ultralytics import YOLO
from pynput.mouse import Button, Controller

# Load the trained YOLO model
model = YOLO('path/to/your/trained/model.pt')

# Capture the screen (you can adjust this part to capture a specific area)
cap = cv2.VideoCapture(0)  # Change this to capture the screen

mouse = Controller()

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Perform detection
    results = model(frame)

    # Draw bounding boxes and find the 'close' button
    for result in results:
        for box in result.boxes:
            x1, y1, x2, y2 = box.xyxy[0]
            if box.cls == 'close_button':  # Assuming 'close_button' is your label
                cv2.rectangle(frame, (x1, y1), (x2, y2), (255, 0, 0), 2)
                # Simulate a mouse click on the 'close' button
                mouse.position = ((x1 + x2) / 2, (y1 + y2) / 2)
                mouse.click(Button.left, 1)

    cv2.imshow('Frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
