from django.urls import path
from . import views

urlpatterns = [
    path('gender/', views.UserGenderView.as_view(), name='users'),
    path('age/', views.UserAge.as_view(), name='users'),
    path('weight/', views.UserWeight.as_view(), name='weight'),
    path('friend/', views.UserFriend.as_view(), name='friend'),
    path('heartbeats/', views.HeartbeatListCreate.as_view(), name='heartbeats'),
    path('sleep_data/', views.SleepDataListCreate.as_view(), name='sleep_data'),
]
