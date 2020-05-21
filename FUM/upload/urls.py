from django.urls import path

from File_Upload_Management.upload.migrations import views

urlpatterns = [
    path('', views.index, name='index'),
]