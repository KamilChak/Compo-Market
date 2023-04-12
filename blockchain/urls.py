from django.urls import path
from . import views

app_name = 'blockchain'
urlpatterns = [
    path('transaction/', views.transaction, name='transaction'),
    path('get_chain/', views.display_chain, name='get_chain'),
]
