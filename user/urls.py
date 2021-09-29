from . import views

from django.urls import path
from django.contrib.auth import views as auth_views
urlpatterns = [
    
    path('', auth_views.LoginView.as_view(template_name='user/login.html'), name='login'),
    path('register/', views.userRegister, name='register'),
    path('logout/',auth_views.LogoutView.as_view(template_name='user/logout.html'), name='logout'),
    path('profile/', views.profile, name='profile'),
    path('editPassword/', views.change_Pass, name='editPassword'),
    path('admincustom/', views.adminView, name='admincustom'),
]