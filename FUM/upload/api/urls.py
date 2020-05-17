from .views import FUMRead, ModuleRead, ContactRead, FUMCreate, FileListAPIView

from django.contrib import admin
from django.urls import path, include, re_path

app_name = 'upload'

urlpatterns = [
    path('', FileListAPIView.as_view(), name='file-list'),
    path('create/', FUMCreate.as_view(), name='upload-create'),
    path('<int:collaborate_files_a00_rec>/', FUMRead.as_view(), name='upload-read'),
    #path('module/<int:pk>/', ModuleRead.as_view(), name='module-read'),
    #path('contact/<int:pk>/', ContactRead.as_view(), name='contact-read'),
]