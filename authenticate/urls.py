from django.urls import path
from . import views

app_name = 'authenticate'
urlpatterns = [
    path('', views.welcome, name='welcome'),
    path('home/', views.home, name='home'),
    path('compo_sign/', views.CompoSignView.as_view(), name='compo_sign'),
]
