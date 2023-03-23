from django.urls import path
from . import views

app_name = 'compoAccount'
urlpatterns = [
    path('', views.dashboard, name='dashboard'),

]
