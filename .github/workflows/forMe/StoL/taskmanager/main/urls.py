from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name = 'Global' ),
    path ('about',views.about, name = 'about'),
    path ('list_E',views.list_E, name = 'list_E')
]
