from django.shortcuts import render
from turbo.models import Car, CarImages
from turbo.serializers import CarSerializer, ImageSerializer
from rest_framework.generics import ListAPIView

class CarListView(ListAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer


class ImagesListView(ListAPIView):
    queryset = CarImages.objects.all()
    serializer_class = ImageSerializer