from turtle import home
from django.urls import path
from .views import HomeView,WaitingCreate,WaitingListView,WaitingDelete

app_name = "standby"

urlpatterns = [
    path('',HomeView.as_view(),name='home'),
    path('add_waiting/',WaitingCreate.as_view(),name='add_waiting'),
    path('waiting_list/<name>',WaitingListView.as_view(),name='waiting_list'),
    path('delete_waiting/<int:pk>',WaitingDelete.as_view()),

]