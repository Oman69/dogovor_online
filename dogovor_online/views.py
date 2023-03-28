from typing import Dict

from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from .models import ObjectByDogovor


def home(request):
    objects = ObjectByDogovor.objects.all()
    context = {
        'Objects': objects,
    }
    return render(request, 'dogovor_online/home.html', context)


def room(request, dogovor):
    return render(request, 'dogovor_online/room.html')


def garage(request, dogovor):
    return render(request, 'dogovor_online/garage.html')


def auto(request, dogovor):
    return render(request, 'dogovor_online/auto.html')

def zemlya(request, dogovor):
    return render(request, 'dogovor_online/zemlya.html')


def services(request, dogovor):
    return render(request, 'dogovor_online/services.html')


def show_deal(request):
    sername_1 = request.POST['sername_1']
    name_1 = request.POST['name_1']
    return HttpResponse(f'{sername_1} {name_1}')
