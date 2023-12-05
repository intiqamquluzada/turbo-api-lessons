from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response

from turbo.models import Car, CarImages
from turbo.serializers import CarSerializer, ImageSerializer
from rest_framework.generics import (ListAPIView, RetrieveAPIView, CreateAPIView,
                                     UpdateAPIView, DestroyAPIView)


class CarListView(ListAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer


class CarDetailView(RetrieveAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
    lookup_field = 'slug'

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.user_view_count += 1
        instance.save()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)


class CarCreateView(CreateAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer

    # def post(self, request, *args, **kwargs):
    #     serializer = self.get_serializer(data=request.data)
    #     print(serializer.errors)
    #     serializer.is_valid(raise_exception=True)
    #     self.perform_create(serializer)
    #     headers = self.get_success_headers(serializer.data)
    #     return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
    #

class CarUpdateView(UpdateAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
    lookup_field = 'slug'


class DeleteCarView(DestroyAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
    lookup_field = 'slug'


class CarImagesListView(ListAPIView):
    queryset = CarImages.objects.all()
    serializer_class = ImageSerializer


class CarImageCreate(CreateAPIView):
    queryset = CarImages.objects.all()
    serializer_class = ImageSerializer


# FILTER, PAGINATION, ACCOUNT-> create, Selection