# ObjectDetector/views.py

from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser
from .utils import run_detection  # assuming you have detection logic here

class ObjectDetectionView(APIView):
    parser_classes = [MultiPartParser]

    def post(self, request, *args, **kwargs):
        image = request.FILES.get('image')
        if not image:
            return Response({'error': 'No image uploaded'}, status=400)

        result = run_detection(image)  # assume your model returns JSON
        return Response(result)

def upload_form(request):
    if request.method == "POST" and "image" in request.FILES:
        result = run_detection(request.FILES["image"])
        return render(request, "upload.html", {
            "image_url": result["image_url"],
            "detections": result["detections"]
        })

    return render(request, "upload.html")
