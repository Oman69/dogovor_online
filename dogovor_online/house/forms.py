from django import forms


class HouseForm(forms.Form):
    # Характеристики квартиры
    kadastr_number = forms.CharField(max_length=100, label='Кадастровый номер дома')
    apart_address = forms.CharField(max_length=200, label='Адрес дома')
    full_space = forms.FloatField(label='Общая площадь дома')
    life_space = forms.FloatField(label='Жилая площадь дома')
    floor = forms.IntegerField(max_value=50, label='Количество этажей')
    registered = forms.ChoiceField(choices=(('No', 'Нет'), ('Yes', 'Да'),), label='Зарегистрированные лица')
    arested = forms.ChoiceField(choices=(('No', 'Нет'), ('Yes', 'Да'),), label='Обременения')
