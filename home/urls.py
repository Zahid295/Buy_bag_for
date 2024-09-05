from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('check_db_connection/', views.check_db_connection, name='check_db_connection'),
]