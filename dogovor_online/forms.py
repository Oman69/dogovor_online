from django import forms

# Формы для объектов договора

class ZemlyaForm(forms.Form):
    kadastr_number_zemlya = forms.CharField(max_length=100, label='Кадастровый номер земельного участка')
    zemlya_address = forms.CharField(max_length=200, label='Адрес земельного участка')
    zemlya_space = forms.FloatField(label='Площадь земельного участка')
    arested = forms.ChoiceField(choices=(('No', 'Нет'), ('Yes', 'Да'),), label='Обременения')


# Формы для видов договора
class SaleForm(forms.Form):
    date = forms.DateField(label='Дата подписания договора')
    location = forms.CharField(max_length=100, label='Место подписания договора')
    deal_number = forms.CharField(max_length=100, label='Номер договора')
    payment = forms.ChoiceField(choices=(('Cash', 'Наличные'), ('Online', 'Банковский перевод'), ('Accredit', 'Аккредитив'),), label='Оплата')
    price_digit = forms.IntegerField(label='Цена продажи цифрами')
    price_string = forms.CharField(max_length=200, label='Цена продажи прописью')


class NaimForm(forms.Form):
    pass


class FreeForm(forms.Form):
    pass


class BankForm(forms.Form):
    pass


class RentForm(forms.Form):
    pass