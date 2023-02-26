from django.urls import path

from dogovor_online import views

urlpatterns = [
    path('', views.home, name='home'),
    # Квартира
    path('apartment/<slug:dogovor>/', views.apartment, name='apartment'),
    # Жилой дом
    path('house/<slug:dogovor>/', views.house, name='house'),
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

]