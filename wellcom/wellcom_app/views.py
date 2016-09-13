from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def all_wells(request):
    return render(request, 'all_wells.html')


def well_detail(request):
    return render(request, 'well_detail.html')
