from . import views
from django.urls import path

urlpatterns = [
    path('', views.home, name="home_view"),
    path('request/', views.algorithm, name="algorithm"),
    path('request/<str:place_name>', views.detail_view, name="detail")
]