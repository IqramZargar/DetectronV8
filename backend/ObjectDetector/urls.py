# ObjectDetector/urls.py

from django.urls import path
from .views import ObjectDetectionView, upload_form

urlpatterns = [
    path('detect/', ObjectDetectionView.as_view(), name='object-detect'),
    path('', upload_form, name='upload-form'),  # basic upload form view
]
