from . import views
from django.urls import path

urlpatterns = [
    path('add/', views.add_profile, name = 'add_profile'),
]
