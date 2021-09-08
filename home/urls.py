from django.urls import path
from . import views
from .views import UsersListView, UsersDetailView, follow_action, random_picture

urlpatterns = [
    path('', UsersListView.as_view(), name='home'),
    path('profile_info/<int:pk>/', UsersDetailView.as_view(), name='profile_info'),
    path('follow/', follow_action, name='following'),
    path('random_picture/', random_picture, name='random_picture')
]