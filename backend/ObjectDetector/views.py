from django.shortcuts import render
from django.conf import settings
import os
from ultralytics import YOLO   # make sure you have ultralytics installed

# Load YOLO model once
model = YOLO("yolov8n.pt")   # or your custom model

def detection_view(request):
    context = {}
    if request.method == "POST":
        img = request.FILES.get("image")
        if img:
            # Save uploaded file
            save_path = os.path.join(settings.MEDIA_ROOT, img.name)
            with open(save_path, "wb+") as f:
                for chunk in img.chunks():
                    f.write(chunk)

            # Run YOLO detection
            results = model(save_path)

            # Create a processed filename
            processed_filename = f"processed_{img.name}"
            processed_path = os.path.join(settings.MEDIA_ROOT, processed_filename)

            # Save result image with bounding boxes
            results[0].save(filename=processed_path)

            # Extract detections for display
            detections = []
            for box in results[0].boxes:
                cls_id = int(box.cls[0].item())
                conf = float(box.conf[0].item())
                label = results[0].names[cls_id]
                detections.append({
                    "label": label,
                    "confidence": f"{conf:.2f}"
                })

            # Pass context to template
            context = {
                "image_url": settings.MEDIA_URL + processed_filename,
                "detections": detections,
            }

    return render(request, "detection.html", context)
