from . import views
from django.urls import path

urlpatterns = [
    path('', views.home, name="home_view"),
    path('request/', views.algorithm, name="algorithm"),
]