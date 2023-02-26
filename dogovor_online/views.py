from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from .models import ObjectByDogovor, Dogovor
from .forms import PartyFl_1_Form, PartyFl_2_Form, ApartmentForm, HouseForm, SaleForm


def home(request):
    objects = ObjectByDogovor.objects.all()
    context = {
        'Objects': objects,
    }
    return render(request, 'dogovor_online/home.html', context)


def apartment(request, dogovor):
    if request.method == 'POST':

        party1form = PartyFl_1_Form(request.POST)
        party2form = PartyFl_2_Form(request.POST)
        apartmentForm = ApartmentForm(request.POST)


        if dogovor == 'sale':
            dealForm = SaleForm(request.POST)
        elif dogovor == 'naim':
            pass
        elif dogovor == 'darenie':
            pass
        elif dogovor == 'ipoteka':
            pass
        else:
            pass

        # check whether it's valid:
        if party1form.is_valid() and party2form.is_valid() and apartmentForm.is_valid() and dealForm.is_valid():
            return HttpResponse('Форма отправлена!')
    else:
        party1form = PartyFl_1_Form()
        party2form = PartyFl_2_Form()
        apartmentForm = ApartmentForm()
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
        'apartmentForm': apartmentForm,
        'dealForm': dealForm
    }


    return render(request, 'dogovor_online/apartment.html', context)


def house(request, dogovor):
    if request.method == 'POST':

        party1form = PartyFl_1_Form(request.POST)
        party2form = PartyFl_2_Form(request.POST)
        houseForm = HouseForm(request.POST)

        if dogovor == 'sale':
            dealForm = SaleForm(request.POST)
        elif dogovor == 'naim':
            pass
        elif dogovor == 'darenie':
            pass
        elif dogovor == 'ipoteka':
            pass
        else:
            pass

        # check whether it's valid:
        if party1form.is_valid() and party2form.is_valid() and houseForm.is_valid() and dealForm.is_valid():
            return HttpResponse('Форма отправлена!')
    else:
        party1form = PartyFl_1_Form()
        party2form = PartyFl_2_Form()
        houseForm = HouseForm()
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
        'object': 'дома',
        'deal': deal,
        'seotitle': 'онлайн бесплатно без регистрации',
        'party1': party1,
        'party2': party2,
        'party1form': party1form,
        'party2form': party2form,
        'apartmentForm': houseForm,
        'dealForm': dealForm
    }
    return render(request, 'dogovor_online/house.html', context)




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

