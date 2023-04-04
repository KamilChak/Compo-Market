from django import forms
from .models import Composter
from django.contrib.gis.forms import OSMWidget
class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    confirm_password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = Composter
        fields = ['username', 'email', 'password', 'confirm_password']


    def clean_username(self):
        username = self.cleaned_data.get('username')
        if Composter.objects.filter(username=username).exists():
            raise forms.ValidationError('This username is already in use.')
        return username

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
    

class PointForm(forms.ModelForm):
    class Meta:
        model = Composter
        fields = ['point']
        widgets = {
            'point': OSMWidget(attrs={
                'map_height': 500,
                'map_width': 800,
                'map_srid': 4326,
                'default_zoom': 5,
                'default_lat': 37.213874,
                'default_lon': 10.126849,
            }),
        }