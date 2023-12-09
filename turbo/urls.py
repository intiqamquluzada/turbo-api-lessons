from django.urls import path
from turbo.views import *

urlpatterns = [
    path("", CarListView.as_view(), name='car-list'),
    path("detail/<slug>/", CarDetailView.as_view(), name='car-detail'),
    path("create/", CarCreateView.as_view(), name='car-create'),
    path("images/", CarImagesListView.as_view(), name='images'),
    path("update/car/<slug>/", CarUpdateView.as_view(), name='car-update'),
    path("delete/car/<slug>/", DeleteCarView.as_view(), name='delete-car'),
    path("create/images/", CarImageCreate.as_view(), name='car-image-create'),

]