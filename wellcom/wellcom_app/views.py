from django.shortcuts import render, get_object_or_404
from .serializers import WellSerializer, NoteSerializer, DeviceDataSerializer
from .serializers import UsageSerializer, WaterTestSerializer
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
    wells = Well.objects.all()
    context = {
        'wells': wells,
    }
    return render(request, 'index.html', context)


def all_wells(request):
    wells = Well.objects.all()
    context = {
        'wells': wells,
    }
    return render(request, 'all_wells.html', context)


def well_detail(request, well_id):
    wells = Well.objects.all()
    well = get_object_or_404(Well, id=well_id)
    try:
        water_tests = well.watertest_set.all()
    except:
        water_tests = None
        print("No tests for this well")
    context = {
        'wells': wells,
        'well': well,
        'water_tests': water_tests,
    }
    return render(request, 'well_detail.html', context)
