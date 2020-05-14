from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    path('', views.HomeView.as_view(), name='home_cbv'),
    path('home/', views.home, name='home_fbv'),
]
