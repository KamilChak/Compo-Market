from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('authenticate.urls')),
    path('compoAccount/', include('compoAccount.urls')),
    path('greenerAccount/', include('greenerAccount.urls')),
    path('blockchain/', include('blockchain.urls')),
]