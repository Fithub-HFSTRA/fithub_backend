from django.urls import path
from . import views

urlpatterns = [
    path('gender', views.UserGenderView.as_view(), name='users'),
]
