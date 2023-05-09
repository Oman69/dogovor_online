from django import forms


class ApartmentForm(forms.Form):
    # Характеристики квартиры
    kadastr_number = forms.CharField(max_length=100, label='Кадастровый номер')
    apart_address = forms.CharField(max_length=200, label='Адрес квартиры')
    full_space = forms.FloatField(label='Общая площадь')
    floor = forms.IntegerField(max_value=50, label='Этаж')
    rooms = forms.IntegerField(max_value=50, label='Количество комнат')
    registered = forms.ChoiceField(choices=(('No', 'Нет'), ('Yes', 'Да'),), label='Есть ли зарегистрированные лица')
    arested = forms.ChoiceField(choices=(('No', 'Нет'), ('Yes', 'Да'),), label='Есть ли обременения')
