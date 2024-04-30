from django.urls import path
from . import views

urlpatterns = [
    path('userinfo/', views.UserInfoView.as_view(), name='users'),
    path('plan/', views.UserPlan.as_view(), name='users'),
    path('wktypes/', views.UserWorkoutTypes.as_view(), name='workout_types'),
    path('gender_update/', views.UserGenderView.as_view(), name='users'),
    path('age_update/', views.UserAge.as_view(), name='users'),
    path('weight_update/', views.UserWeight.as_view(), name='weight'),
    path('friend/', views.UserFriend.as_view(), name='friend'),
    path('heartbeat_update/', views.HeartbeatSummary.as_view(), name='heartbeat'),
    path('sleep_data/', views.SleepData.as_view(), name='sleep_data'),
    path('name_update/', views.NameData.as_view(), name='users'),
    path('signup/', views.SignupView.as_view(), name='signup'),
    path('exercise_all/', views.getAllExercises.as_view(), name='excercises'),
    path('strt_ex/', views.startExercise.as_view(), name='start excercises'),
    path('end_ex/', views.endExercise.as_view(), name='end excercises'),
    path('get_feed/', views.FriendFeed.as_view(), name='end excercises'),

]