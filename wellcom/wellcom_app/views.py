from django.shortcuts import render
from .serilaizers import WellSerializer, NoteSerializer, DeviceDataSerializer
from .serilaizers import UsageSerializer, WaterTestSerializer
from django.views import generic
from rest_framework import viewsets
from .models import Well, Note, DeviceData, Usage, WaterTest


class WellViewSet(viewsets.ModelViewSet):
    queryset = Well.objects.all()
    serializer_class = WellSerializer

class NoteViewSet(viewsets.ModelViewSet):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer

class DeviceDataViewSet(viewsets.ModelViewSet):
    queryset = DeviceData.objects.all()
    serializer_class = DeviceDataSerializer

class UsageViewSet(viewsets.ModelViewSet):
    queryset = Usage.objects.all()
    serializer_class = UsageSerializer

class WaterTestViewSet(viewsets.ModelViewSet):
    queryset = WaterTest.objects.all()
    serializer_class = WaterTestSerializer

def index(request):
    return render(request, 'index.html')


def all_wells(request):
    return render(request, 'all_wells.html')


def well_detail(request):
    return render(request, 'well_detail.html')
