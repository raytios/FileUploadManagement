from django.urls import path

from FUM.upload.migrations import views

urlpatterns = [
    path('', views.index, name='index'),
]