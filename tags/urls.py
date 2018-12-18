from django.urls import path, include
from .import views

app_name = 'tags'
urlpatterns= [
    path('display/', views.display, name='display'),
    path('<int:tag_id>/', views.detail, name='detail'),
]
