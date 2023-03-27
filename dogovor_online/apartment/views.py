from django.shortcuts import render

from dogovor_online.forms import PartyFl_1_Form, PartyFl_2_Form, SaleForm
from dogovor_online.models import Dogovor
from .forms import ApartmentForm


def index(request, dogovor):
    if request.method == 'POST':

        party1form = PartyFl_1_Form(request.POST)
        party2form = PartyFl_2_Form(request.POST)
        typeForm = ApartmentForm(request.POST)

        if dogovor == 'sale':
            dealForm = SaleForm(request.GET)
        elif dogovor == 'naim':
            pass
        elif dogovor == 'darenie':
            pass
        elif dogovor == 'ipoteka':
            pass
        else:
            pass

    else:
        party1form = PartyFl_1_Form()
        party2form = PartyFl_2_Form()
        typeForm = ApartmentForm()
        dealForm = SaleForm()

    deal = Dogovor.objects.get(url=dogovor)

    if dogovor in ('sale', 'ipoteka'):
        party1 = 'Продавец'
        party2 = 'Покупатель'
    elif dogovor == 'naim':
        party1 = 'Наймодатель'
        party2 = 'Наниматель'
    elif dogovor == 'darenie':
        party1 = 'Даритель'
        party2 = 'Одаряемый'
    else:
        party1 = 'Сторона 1'
        party2 = 'Сторона 2'

    context = {
        'object': 'квартиры',
        'deal': deal,
        'seotitle': 'онлайн бесплатно без регистрации',
        'party1': party1,
        'party2': party2,
        'party1form': party1form,
        'party2form': party2form,
        'typeForm': typeForm,
        'dealForm': dealForm,
    }

    return render(request, 'dogovor_online/apartment.html', context)
