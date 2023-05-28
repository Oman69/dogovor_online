from django.shortcuts import render
from dogovor_online.models import Dogovor, ObjectByDogovor
from dogovor_online.views import get_forms_type
from sale import string_to_data
from django.http import HttpResponse


def apartment(request, dogovor):
    params = get_forms_type(request)
    objects = ObjectByDogovor.objects.all()
    deal = Dogovor.objects.get(url=dogovor).name

    context = {
        'object': 'квартиры',
        'deal': deal,
        'seotitle': 'онлайн бесплатно без регистрации',
        'party1': params['types'][dogovor][1],
        'party2': params['types'][dogovor][2],
        'party1form': params['party1form'],
        'party2form': params['party2form'],
        'typeForm': params['typeForm']['apartment'],
        'dealForm': params['types'][dogovor][0],
        'Objects': objects
    }

    string_to_data(context)
    return render(request, 'dogovor_online/form.html', context)
