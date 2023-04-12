from django.contrib import admin
from .models import Composter, Greener

# Register your models here.
@admin.register(Composter)
class ComposterAdmin(admin.ModelAdmin):
    list_display = ('id', 'orgName', 'email', 'composter_location')

@admin.register(Greener)
class GreenerAdmin(admin.ModelAdmin):
    list_display = ('id', 'firstName', 'lastName', 'email', 'wallet')
