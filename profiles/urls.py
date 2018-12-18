from django.urls import include, path
from . import views
from django.contrib.auth import views as auth_views



app_name = 'profiles'
urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='profiles/login.html'), name = 'login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='profiles/logout.html'), name='logout'),
    path('profile/', views.profile, name='profile'),
    path('edit/', views.profileUpdate, name='edit'),
    path('register/', views.register, name='register'),
]
