from django import forms
from .models import Composter, Greener
from django.contrib.gis.forms import OSMWidget
from django.forms import widgets
from django.contrib.gis import forms as geoforms

class ComposterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    confirm_password = forms.CharField(widget=forms.PasswordInput())

    orgName = forms.CharField(label="Organization's name")

    class Meta:
        model = Composter
        fields = ['orgName', 'email', 'password', 'confirm_password']


    def clean_orgName(self):
        orgName = self.cleaned_data.get('orgName')
        if Composter.objects.filter(orgName=orgName).exists():
            raise forms.ValidationError('This name is already in use.')
        return orgName

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if Composter.objects.filter(email=email).exists():
            raise forms.ValidationError('This email address is already in use.')
        return email

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')

        if password and confirm_password and password != confirm_password:
            raise forms.ValidationError("Passwords do not match.")
        print('clean method called')
        return cleaned_data
    

class ComposterLocationForm(forms.ModelForm):

    class Meta:
        model = Composter
        fields = ['composter_location']
        labels = {
            'composter_location': 'Submit your Location'
        }
        widgets = {
            'composter_location': OSMWidget(attrs={
                'map_height': 500,
                'map_width': 800,
                'map_srid': 4326,
                'default_zoom': 6,
                'default_lat': 34.702310,
                'default_lon': 9.356161,
            }),
        }

class GreenerForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    confirm_password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = Greener
        fields = ['firstName', 'lastName', 'email', 'password', 'confirm_password']


    def clean_email(self):
        email = self.cleaned_data.get('email')
        if Greener.objects.filter(email=email).exists():
            raise forms.ValidationError('This email address is already in use.')
        return email

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')

        if password and confirm_password and password != confirm_password:
            raise forms.ValidationError("Passwords do not match.")
        print('clean method called')
        return cleaned_data
    

class GreenerLocationForm(forms.ModelForm):

    class Meta:
        model = Greener
        fields = ['greener_location']
        labels = {
            'greener_location': 'Submit your Location'
        }
        widgets = {
            'greener_location': OSMWidget(attrs={
                'map_height': 500,
                'map_width': 800,
                'map_srid': 4326,
                'default_zoom': 6,
                'default_lat': 34.702310,
                'default_lon': 9.356161,
            }),
        }

class MapForm(forms.Form):
    greener_location = forms.CharField(widget=OSMWidget(
        attrs={'map_width': 800, 'map_height': 500,'default_zoom': 8, 'default_lat': 34.702310, 'default_lon': 9.356161}))
