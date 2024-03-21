from django.urls import path
from . import views

urlpatterns = [
    path('userinfo/', views.UserInfoView.as_view(), name='users'),
    path('gender/', views.UserGenderView.as_view(), name='users'),
    path('age/', views.UserAge.as_view(), name='users'),
    path('weight/', views.UserWeight.as_view(), name='weight'),
    path('friend/', views.UserFriend.as_view(), name='friend'),
    path('heartbeat/', views.HeartbeatSummary.as_view(), name='heartbeat'),
    path('sleep_data/', views.SleepData.as_view(), name='sleep_data'),
]
