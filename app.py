from flask import Flask, request, jsonify, render_template
from flask_socketio import SocketIO, emit
from ultralytics import YOLO
import cv2
import numpy as np
from PIL import Image
import io
import base64

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your-secret-key-here'
socketio = SocketIO(app, cors_allowed_origins="*")

# Load YOLOv11 model
model = YOLO("yolo11x.pt")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/health', methods=['GET'])
def health():
    return jsonify({"status": "healthy", "model": "YOLOv11"}), 200

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Check if image is uploaded
        if 'image' not in request.files:
            return jsonify({"error": "No image file provided"}), 400
        
        file = request.files['image']
        
        if file.filename == '':
            return jsonify({"error": "No file selected"}), 400
        
        # Read image
        image_bytes = file.read()
        image = Image.open(io.BytesIO(image_bytes))
        image_np = np.array(image)
        
        # Convert RGB to BGR for OpenCV
        if len(image_np.shape) == 3:
            image_np = cv2.cvtColor(image_np, cv2.COLOR_RGB2BGR)
        
        # Run detection
        results = model(image_np)
        
        # Get detection results
        detections = []
        for result in results:
            boxes = result.boxes
            for box in boxes:
                detection = {
                    "class": int(box.cls[0]),
                    "confidence": float(box.conf[0]),
                    "bbox": box.xyxy[0].tolist()
                }
                detections.append(detection)
        
        # Create annotated image
        annotated_frame = results[0].plot()
        
        # Convert annotated image to base64
        _, buffer = cv2.imencode('.jpg', annotated_frame)
        img_base64 = base64.b64encode(buffer).decode('utf-8')
        
        return jsonify({
            "detections": detections,
            "annotated_image": f"data:image/jpeg;base64,{img_base64}",
            "num_detections": len(detections)
        }), 200
        
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@socketio.on('frame')
def handle_frame(data):
    try:
        # Decode base64 image
        image_data = data['image'].split(',')[1]
        image_bytes = base64.b64decode(image_data)
        nparr = np.frombuffer(image_bytes, np.uint8)
        frame = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
        
        # Run detection
        results = model(frame, verbose=False)
        
        # Create annotated frame
        annotated_frame = results[0].plot()
        
        # Convert to base64
        _, buffer = cv2.imencode('.jpg', annotated_frame, [cv2.IMWRITE_JPEG_QUALITY, 85])
        img_base64 = base64.b64encode(buffer).decode('utf-8')
        
        # Get detection info
        detections = []
        for result in results:
            boxes = result.boxes
            for box in boxes:
                detection = {
                    "class": int(box.cls[0]),
                    "confidence": float(box.conf[0]),
                    "bbox": box.xyxy[0].tolist()
                }
                detections.append(detection)
        
        # Send back annotated frame
        emit('detection_result', {
            'image': f"data:image/jpeg;base64,{img_base64}",
            'detections': detections,
            'count': len(detections)
        })
        
    except Exception as e:
        emit('error', {'message': str(e)})

@socketio.on('stop_camera')
def handle_stop():
    emit('camera_stopped', {'status': 'success'})

if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=5000, debug=False, allow_unsafe_werkzeug=True)

