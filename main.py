from ultralytics import YOLO
import cv2

# Load YOLOv11 model
model = YOLO("yolo11x.pt")

# Open webcam
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Run detection
    results = model(frame)

    # Draw boxes and labels
    annotated_frame = results[0].plot()

    # Show output
    cv2.imshow("YOLOv11 Detection", annotated_frame)

    # Exit when 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
