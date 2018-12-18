from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .import views
from django.contrib.auth import views as auth_views
#from .views import PostCreateView
from .views import EventUpdateView, EventDetailView, EventDeleteView
app_name = 'event'
urlpatterns= [
    path('create/', views.create, name='create'),
    #path('create/', PostCreateView.as_view(), name='create'),
    path('home/', views.home, name='home'),
    path('<int:pk>/', EventDetailView.as_view(), name='detail'),
    #path('<int:event_id>/edit', views.edit, name='edit'),
    #changed from <int:event id to int:pk> and it works!
    path("<int:pk>/edit/", EventUpdateView.as_view(), name='event_edit'),
    #path('<int:pk>/delete/', EventDeleteView.as_view(), name='event_delete'),
    path('<int:event_id>/delete/', views.delete, name='event_delete'),
    path('<int:event_id>/attend/', views.attend, name='attend'),
    path('<int:event_id>/unattend/', views.unattend, name='unattend'),
]
