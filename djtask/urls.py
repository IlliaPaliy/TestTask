from django.contrib import admin
from django.contrib.auth import views as authviews
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from users import views as usersviews
from home.views import UsersListView, UsersDetailView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('home/', UsersListView.as_view(), name='home'),
    path('register/', usersviews.register, name="register"),
    path('login/', authviews.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', authviews.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('profile/', usersviews.profile, name='profile'),
    path('profile_info/<int:pk>/', UsersDetailView.as_view(), name='profile_info'),
    path('change_profile/',usersviews.change_profile, name='change_profile'),
    path('password_reset/', authviews.PasswordResetView.as_view(template_name='users/password_reset.html'), name="password_reset"),
    path('password_reset/done/', authviews.PasswordResetDoneView.as_view(template_name='users/password_reset_done.html'), name="password_reset_done"),
    path('password_reset_confirm/<uidb64>/<token>/', authviews.PasswordResetConfirmView.as_view(template_name='users/password_reset_confirm.html'), name="password_reset_confirm"),
    path('password_reset_complete/', authviews.PasswordResetCompleteView.as_view(template_name='users/password_reset_complete.html'), name="password_reset_complete")


]
 

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 