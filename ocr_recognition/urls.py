"""
ocr URL Configuration
"""
from django.conf.urls import url, include
from ocr_recognition import views

urlpatterns = [
    # OCR
    url(r'^ocr/$', views.ocr),
]