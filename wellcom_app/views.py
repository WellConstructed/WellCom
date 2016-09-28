from django.shortcuts import render, get_object_or_404
from .serializers import (WellSerializer, NoteSerializer, DeviceDataSerializer,
                          DeviceOutputSerializer, UsageSerializer,
                          WaterTestSerializer, TestSerializer,
                          HourlyUsageSerializer,
                          WellNameHourlyUsageSerializer)
from django.views import generic
from rest_framework import viewsets, generics, filters
from .models import (Well, Note, DeviceData, Usage, WaterTest, Test,
                     DeviceOutput, HourlyUsage)
from django.views.decorators.cache import cache_page
from django.db.models import Avg, Count, Sum, F
from django.db.models.functions import TruncDate
from django.http import JsonResponse

class WellViewSet(viewsets.ModelViewSet):
    queryset = Well.objects.all()
    serializer_class = WellSerializer


# class WellNameViewSet(viewsets.ModelViewSet):
#     #  TODO: We should only pull well id and name
#     queryset = Well.objects.all()
#     serializer_class = WellNameSerializer


class NoteViewSet(viewsets.ModelViewSet):
    queryset = Note.objects.all().order_by('-created')
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


class TestViewSet(viewsets.ModelViewSet):
    queryset = Test.objects.all()
    serializer_class = TestSerializer


class DeviceOutputViewSet(viewsets.ModelViewSet):
    queryset = DeviceOutput.objects.all()
    serializer_class = DeviceOutputSerializer


class WellNameHourlyUsageViewSet(viewsets.ModelViewSet):
    queryset = Well.objects.all()
    serializer_class = WellNameHourlyUsageSerializer


class HourlyUsageViewSet(viewsets.ModelViewSet):
    queryset = HourlyUsage.objects.all()
    serializer_class = HourlyUsageSerializer

    def get_queryset(self):
        well_id = self.request.query_params.get("well", None)
        queryset = HourlyUsage.objects.all()
        print("WELL ID", well_id)

        # print("well_names", well_names)
        if well_id is None:
            for hourly in queryset:
                pass
                # print(wellget_well_name_id_dict)
        else:
            print("well is not none")
            name = Well.objects.get(pk=well_id)
            print("name", name)
            queryset = queryset.filter(well=well_id).annotate(name=name)
        print(queryset)
        return queryset


# @cache_page(86400)
def about_us(request):
    wells = Well.objects.all()

    context = {
        'wells': wells,

    }
    return render(request, 'about_us.html', context)


# @cache_page(86400)
def wells(request):
    wells = Well.objects.all()
    # avg_date = HourlyUsage.objects.order_by(well_id='id').annotate(date=TruncDate('timestamp')).aggregate(avg=Sum('usage_count')/Count('date', distinct=True))
    context = {
        'wells': wells,
        # 'avg_date': avg_date
    }
    return render(request, 'wells.html', context)


# @cache_page(86400)
def well_detail(request, well_id):
    wells = Well.objects.all()
    well = get_object_or_404(Well, id=well_id)
    total_use = HourlyUsage.objects.filter(
                            well_id=well.id).aggregate(sum=Sum('usage_count'))
    try:
        water_tests = well.watertest_set.all()
    except:
        water_tests = None
    try:
        device_data = well.devicedata_set.all()
    except:
        device_data = None
    try:
        notes = well.note_set.all().order_by('-created')
    except:
        notes = None
    context = {
        'wells': wells,
        'well': well,
        'water_tests': water_tests,
        'device_data': device_data,
        'notes': notes,
        'total_use': total_use
    }
    return render(request, 'well_detail.html', context)


def test_device_view(request):
    device_data = DeviceData.objects.all()
    # hourly_events = device_data.objects.filter(Timestamp_range=(start ))

    context = {
        'device_data': device_data,
    }
    return render(request, 'test_device_data.html', context)


# def well_name_view(request):
#     if request.method == "GET":
#         data = Well.objects.values('id', 'name')
#         # data = [{'id': person.name, 'surname': person.surname} for person in queryset]
#         return render(request, JsonResponse(data, safe=False)
