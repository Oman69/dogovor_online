from django.contrib import admin

from dogovor_online.models import Dogovor, ObjectByDogovor

# Register your models here.
admin.site.register(Dogovor)
admin.site.register(ObjectByDogovor)