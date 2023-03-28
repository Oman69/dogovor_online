from django.shortcuts import render
from dogovor_online.parties.forms import PartyFl_1_Form, PartyFl_2_Form
from dogovor_online.forms import SaleForm, RentForm, FreeForm, BankForm, NaimForm
from dogovor_online.models import Dogovor
from .forms import HouseForm


def house(request, dogovor):
    deal = Dogovor.objects.get(url=dogovor).name
    if request.method == 'POST':
        cur_responce = request.POST
    else:
        cur_responce = request.GET

    types = {'sale': [SaleForm(cur_responce), 'Продавец', 'Покупатель'],
             'naim': [NaimForm(cur_responce), 'Наймодатель', 'Наниматель'],
             'arenda': [RentForm(cur_responce), 'Арендодатель', 'Арендатор'],
             'darenie': [FreeForm(cur_responce), 'Даритель', 'Одаряемый'],
             'ipoteka': [BankForm(cur_responce), 'Продавец', 'Покупатель']}
    party1form = PartyFl_1_Form(cur_responce)
    party2form = PartyFl_2_Form(cur_responce)
    typeForm = HouseForm(cur_responce)

    context = {
        'object': 'частного дома',
        'deal': deal,
        'seotitle': 'онлайн бесплатно без регистрации',
        'party1': types[dogovor][1],
        'party2': types[dogovor][2],
        'party1form': party1form,
        'party2form': party2form,
        'typeForm': typeForm,
        'dealForm': types[dogovor][0],
    }

    return render(request, 'dogovor_online/form.html', context)
