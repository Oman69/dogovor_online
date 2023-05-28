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
    registration_2 = forms.CharField(max_length=200, label='Адрес регистрации')