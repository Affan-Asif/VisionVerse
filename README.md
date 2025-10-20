# YOLOv11 Object Detection Web App

A web application for object detection using YOLOv11, deployed on Render.

## Features

- 🎯 Real-time object detection using YOLOv11
- 📹 **Live camera detection** - stream from your webcam with real-time object detection
- 📤 Image upload via drag-and-drop or file selection
- 🖼️ Visual display of detection results with bounding boxes
- 📊 Detailed detection information with confidence scores
- 🎨 Modern, responsive UI
- ⚡ WebSocket-based real-time communication for smooth live detection

## Local Development

### Prerequisites
- Python 3.11+
- pip

### Installation

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Run the application:
```bash
python app.py
```

3. Open your browser and navigate to `http://localhost:5000`

4. (Optional) Run automated tests (in another terminal):
```bash
python test_local.py
```

## Deployment on Render

### Option 1: Using Render Dashboard (Recommended)

1. **Create a new Web Service on Render:**
   - Go to https://dashboard.render.com
   - Click "New +" and select "Web Service"
   - Connect your GitHub repository

2. **Configure the service:**
   - **Name:** yolo-detection (or your preferred name)
   - **Environment:** Docker
   - **Plan:** Free (or choose a paid plan for better performance)
   - **Build Command:** (leave empty, Docker handles this)
   - **Start Command:** (leave empty, Docker handles this)

3. **Deploy:**
   - Click "Create Web Service"
   - Render will automatically build and deploy your application

### Option 2: Using Render Blueprint (render.yaml)

1. **Push your code to GitHub**

2. **Create a new Blueprint on Render:**
   - Go to https://dashboard.render.com
   - Click "New +" and select "Blueprint"
   - Connect your GitHub repository

3. **Render will automatically:**
   - Detect the `render.yaml` file
   - Create and configure the service
   - Deploy your application

## Usage

### Live Camera Mode (Default)
1. Click the "📹 Live Camera" button (default mode)
2. Click "🎥 Start Camera" to begin live detection
3. Allow camera access when prompted
4. Watch real-time object detection on your webcam feed
5. Click "⏹️ Stop Camera" to stop

### Image Upload Mode
1. Click the "📤 Upload Image" button
2. Drag and drop an image or click to select
3. View detection results with bounding boxes

## API Endpoints

### Health Check
```
GET /health
```
Returns the health status of the application.

### Object Detection (Image Upload)
```
POST /predict
Content-Type: multipart/form-data
Body: image file
```
Returns JSON with detection results and annotated image.

**Response:**
```json
{
  "detections": [
    {
      "class": 0,
      "confidence": 0.95,
      "bbox": [x1, y1, x2, y2]
    }
  ],
  "annotated_image": "data:image/jpeg;base64,...",
  "num_detections": 1
}
```

## Model Information

- **Model:** YOLOv11X
- **Model File:** yolo11x.pt
- **Framework:** Ultralytics YOLO

## Performance Notes

- The free tier on Render may have slower cold starts
- First request may take longer as the model loads
- Consider upgrading to a paid plan for better performance
- Model file size is ~200MB, so initial deployment may take a few minutes
- **Live camera mode**: Processes frames at ~10 FPS depending on server resources
- Free tier may experience some latency with live detection

## Troubleshooting

### Slow Performance
- The free tier has limited resources
- First request is slower due to model loading
- Consider using a paid plan for production

### Build Failures
- Ensure all files are committed to your repository
- Check that yolo11x.pt is included in your repo
- Verify Dockerfile syntax

### Memory Issues
- Free tier has 512MB RAM limit
- If you encounter memory errors, upgrade to a paid plan

## License

This project uses YOLOv11 from Ultralytics. Please refer to their license for usage terms.

## Support

For issues with:
- **YOLO model:** https://github.com/ultralytics/ultralytics
- **Render deployment:** https://render.com/docs
- **This application:** Open an issue in the repository

