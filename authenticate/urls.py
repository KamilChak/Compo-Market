from django.urls import path
from . import views

app_name = 'authenticate'
urlpatterns = [
    path('', views.welcome, name='welcome'),
    path('compo_sign/', views.CompoSignView.as_view(), name='compo_sign'),
    path('green_sign/', views.GreenerSignView.as_view(), name='green_sign'),
]
