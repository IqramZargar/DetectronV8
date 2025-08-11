import os
import uuid
import cv2
import numpy as np
from PIL import Image
from ultralytics import YOLO
from django.conf import settings
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile

# Load YOLO model once
model = YOLO("yolov8n.pt")

def run_detection(image_file):
    # Save uploaded image
    unique_name = f"{uuid.uuid4().hex}.jpg"
    relative_path = f"uploads/{unique_name}"
    full_path = os.path.join(settings.MEDIA_ROOT, relative_path)
    default_storage.save(relative_path, ContentFile(image_file.read()))

    # Load and run model
    image_path = os.path.join(settings.MEDIA_ROOT, relative_path)
    results = model(image_path)[0]

    # Convert to OpenCV format
    image = cv2.imread(image_path)

    detections = []
    for box in results.boxes:
        cls_id = int(box.cls[0])
        label = model.names[cls_id]
        conf = float(box.conf[0])

        # Get box coordinates
        x1, y1, x2, y2 = map(int, box.xyxy[0])

        # Draw rectangle
        cv2.rectangle(image, (x1, y1), (x2, y2), (255, 255, 0), 2)

        # Draw filled background for text
        text = f"{label} {conf:.2f}"
        font_scale = 0.6
        thickness = 2
        (w, h), _ = cv2.getTextSize(text, cv2.FONT_HERSHEY_SIMPLEX, font_scale, thickness)
        cv2.rectangle(image, (x1, y1 - h - 10), (x1 + w, y1), (0, 255, 0), -1)

        # Draw text
        cv2.putText(image, text, (x1, y1 - 5), cv2.FONT_HERSHEY_SIMPLEX,
                    font_scale, (0, 0, 0), thickness, cv2.LINE_AA)

        detections.append({
            "label": label,
            "confidence": round(conf, 2),
            "box": [x1, y1, x2, y2]
        })

    # Save annotated image
    result_name = f"result_{unique_name}"
    result_path = f"uploads/{result_name}"
    result_full_path = os.path.join(settings.MEDIA_ROOT, result_path)
    cv2.imwrite(result_full_path, image)

    return {
        "detections": detections,
        "image_url": settings.MEDIA_URL + result_path
    }
