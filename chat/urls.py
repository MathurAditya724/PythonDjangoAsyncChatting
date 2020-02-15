from django.urls import path
from . import views


urlpatterns = [
    path('', views.NewLogin.as_view()),
    path('<user>/', views.room_list, name='room_list'),
    path('<user>/<room_name>/', views.room, name='room'),
]
