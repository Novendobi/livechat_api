from django.urls import path
from . import views

urlpatterns = [
    #path('', views.home, name='home'),
    #path('<str:room_name>/', views.room, name='room'),

    path('api/start/', views.start_convo, name='start_convo'),
    path('api/conversations/<int:convo_id>/', views.get_conversation, name='get_conversation'),
    path('api/conversations/', views.conversations, name='conversations'),
    path('api/userlist/', views.user_list, name='user_list')
]