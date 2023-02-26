from django.db import models

class Dogovor(models.Model):
    name = models.CharField(max_length=100, verbose_name='Договор')
    url = models.CharField(max_length=100, verbose_name='Ссылка')

    def __str__(self):
        return self.name


    class Meta:
        verbose_name = 'Договор'
        verbose_name_plural = 'Договоры'


class ObjectByDogovor(models.Model):
    name = models.CharField(max_length=100, verbose_name='Объект договора')
    sluck = models.CharField(max_length=100, verbose_name='Ссылка')
    dogovors = models.ManyToManyField(Dogovor, related_name='dogovors', verbose_name='Договоры')

    def __str__(self):
        return self.name


    class Meta:
        verbose_name = 'Объект договора'
        verbose_name_plural = 'Объекты договора'

