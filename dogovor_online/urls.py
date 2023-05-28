from django.urls import path
from dogovor_online import views
from dogovor_online.apartment.views import apartment
from dogovor_online.house.views import house


urlpatterns = [
    path('', views.home, name='home'),
    # Квартира
    path('apartment/<slug:dogovor>/', apartment, name='apartment'),
    # Жилой дом
    path('house/<slug:dogovor>/', house, name='house'),
    # Комната
    path('room/<slug:dogovor>/', views.room, name='room'),
    # Гараж
    path('garage/<slug:dogovor>/', views.garage, name='garage'),
    # Автомобиль
    path('auto/<slug:dogovor>/', views.auto, name='auto'),
    # Земля
    path('zemlya/<slug:dogovor>/', views.auto, name='zemlya'),
    # Услуги
    path('services/<slug:dogovor>/', views.services, name='services'),
    # Cформировать договор
    path('show_deal/<slug:dogovor>/', views.show_deal, name='show_deal'),
    # Экспорт в Word
    path('show_deal/to_word/', views.export_to_word, name='to_word'),

]