from typing import Dict

from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render

from .apartment import fish
from .apartment.forms import ApartmentForm
from .forms import SaleForm, NaimForm, RentForm, DarenieForm, BankForm
from .house.forms import HouseForm
from .models import ObjectByDogovor, Dogovor
from .parties.forms import PartyFl_1_Form, PartyFl_2_Form


def home(request):
    objects = ObjectByDogovor.objects.all()
    context = {
        'Objects': objects,
    }
    return render(request, 'dogovor_online/home.html', context)


def get_forms_type(request):
    if request.method == 'POST':
        cur_responce = request.POST
    else:
        cur_responce = request.GET

    # if form.is_valid():
    #     student = form.save(commit=False)
    #     # commit=False tells Django that "Don't send this to database yet.
    #     # I have more things I want to do with it."
    #     student.user = request.user  # Set the user object here
    #     student.save()  # Now you can send it to DB

    types = {'sale': [SaleForm(cur_responce), 'Продавец', 'Покупатель'],
             'naim': [NaimForm(cur_responce), 'Наймодатель', 'Наниматель'],
             'arenda': [RentForm(cur_responce), 'Арендодатель', 'Арендатор'],
             'darenie': [DarenieForm(cur_responce), 'Даритель', 'Одаряемый'],
             'ipoteka': [BankForm(cur_responce), 'Продавец', 'Покупатель']}
    party1form = PartyFl_1_Form(cur_responce)
    party2form = PartyFl_2_Form(cur_responce)
    typeForm = {'house': HouseForm(cur_responce), 'apartment': ApartmentForm(cur_responce)}

    return {'types': types, 'party1form': party1form, 'party2form': party2form, 'typeForm': typeForm}


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


def show_deal(request, dogovor):
    all_params = request.POST
    deal = Dogovor.objects.get(url=dogovor).name

    context = {

        'all_params': all_params,
        'TEXT': fish.text[dogovor],
        'deal': deal
    }
    # return render(request, 'dogovor_online/show_deal.html', context)
    return render(request, f'apartment/{dogovor}.html', context)