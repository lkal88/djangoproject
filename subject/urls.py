from django.urls import path, include
from .import views

app_name = 'subject'
urlpatterns= [
    path('display/', views.display, name='display'),
    path('<int:subject_id>/', views.detail, name='detail'),
]
