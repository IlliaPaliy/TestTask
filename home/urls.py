from django.urls import path
from . import views
from .views import UsersListView, UsersDetailView, follow_action, random_picture

urlpatterns = [
    path('', views.home, name='home'),
    path('follow/', follow_action, name='following'),
    path('random_picture/', random_picture, name='random_picture')
]