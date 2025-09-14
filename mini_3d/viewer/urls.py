from django.urls import path
from . import views

app_name = 'viewer'

urlpatterns = [
    path('', views.home, name='home'),
    path('upload/', views.upload_model, name='upload_model'),
]
