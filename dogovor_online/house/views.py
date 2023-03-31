from django.shortcuts import render
from dogovor_online.parties.forms import PartyFl_1_Form, PartyFl_2_Form
from dogovor_online.forms import SaleForm, RentForm, FreeForm, BankForm, NaimForm
from dogovor_online.models import Dogovor
from .forms import HouseForm
from dogovor_online.views import get_forms_type


def house(request, dogovor):
    deal = Dogovor.objects.get(url=dogovor).name
    params = get_forms_type(request)

    context = {
        'object': 'частного дома',
        'deal': deal,
        'seotitle': 'онлайн бесплатно без регистрации',
        'party1': params['types'][dogovor][1],
        'party2': params['types'][dogovor][2],
        'party1form': params['party1form'],
        'party2form': params['party2form'],
        'typeForm': params['typeForm']['house'],
        'dealForm': params['types'][dogovor][0],
    }

    return render(request, 'dogovor_online/form.html', context)
