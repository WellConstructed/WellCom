from django.shortcuts import render
from .serilaizers import WellSerializer, NoteSerializer, DeviceDataSerializer
from .serilaizers import UsageSerializer, WaterTestSerializer
from django.views import generic
from rest_framework import viewsets, generics
from .models import Well, Note, DeviceData, Usage, WaterTest


class WellViewSet(viewsets.ModelViewSet):
    queryset = Note.objects.all()
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
    wells = Well.objects.all()
    context = {
        'wells': wells,
    }

    return render(request, 'all_wells.html', context)


def well_detail(request):
    wells = Well.objects.all()
    water_tests = WaterTest.objects.all()
    context = {
        'wells': wells,
        'water_tests': water_tests,
    }
    return render(request, 'well_detail.html', context)
