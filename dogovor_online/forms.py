from django import forms

class PartyFl_1_Form(forms.Form):
    # Сторона 1
    sername_1 = forms.CharField(max_length=100, label='Фамилия')
    name_1 = forms.CharField(max_length=100, label='Имя')
    second_name_1 = forms.CharField(max_length=100, label='Отчество')
    pass_seriya_1 = forms.IntegerField(label='Серия паспорта')
    pass_number_1 = forms.IntegerField(label='Номер паспорта')
    pass_given_1 = forms.CharField(max_length=200, label='Кем выдан паспорт')
    pass_given_data_1 = forms.DateField(label='Когда выдан паспорт')
    pass_given_number_1 = forms.CharField(max_length=10, label='Номер подразделения')
    registration_1 = forms.CharField(max_length=200, label='Адрес регистрации')

class PartyFl_2_Form(forms.Form):
    # Сторона 2
    sername_2 = forms.CharField(max_length=100, label='Фамилия')
    name_2 = forms.CharField(max_length=100, label='Имя')
    second_name_2 = forms.CharField(max_length=100, label='Отчество')
    pass_seriya_2 = forms.IntegerField(label='Серия паспорта')
    pass_number_2 = forms.IntegerField(label='Номер паспорта')
    pass_given_2 = forms.CharField(max_length=200, label='Кем выдан паспорт')
    pass_given_data_2 = forms.DateField(label='Когда выдан паспорт')
    pass_given_number_2 = forms.CharField(max_length=10, label='Номер подразделения')
    registration_2 = forms.CharField(max_length=200, label='Адрес регистрации')


# Формы для объектов договора


class HouseForm(forms.Form):
    # Характеристики квартиры
    kadastr_number = forms.CharField(max_length=100, label='Кадастровый номер дома')
    apart_address = forms.CharField(max_length=200, label='Адрес дома')
    full_space = forms.FloatField(label='Общая площадь дома')
    life_space = forms.FloatField(label='Жилая площадь дома')
    floor = forms.IntegerField(max_value=50, label='Количество этажей')
    registered = forms.ChoiceField(choices=(('No', 'Нет'), ('Yes', 'Да'),), label='Зарегистрированные лица')
    arested = forms.ChoiceField(choices=(('No', 'Нет'), ('Yes', 'Да'),), label='Обременения')

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