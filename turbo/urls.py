from django.urls import path
from turbo.views import *

urlpatterns = [
    path("", CarListView.as_view(), name='car-list'),
    path("images/", ImagesListView.as_view(), name='images'),
]