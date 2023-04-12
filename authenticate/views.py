from django.http import HttpResponse
from django.shortcuts import render, redirect
from formtools.wizard.views import SessionWizardView
from .models import Composter, Greener
from .forms import ComposterForm, ComposterLocationForm, GreenerForm, GreenerLocationForm, MapForm

def welcome(request):
    return render(request, 'welcome.html')

class CompoSignView(SessionWizardView):
    form_list = [ComposterForm, ComposterLocationForm]
    
    def get_template_names(self):
        current_step = self.steps.current
        
        template_name_map = {
            '0': 'compo_sign1.html',
            '1': 'compo_sign2.html',
        }
        
        return [template_name_map[current_step]]
    
    def done(self, form_list, **kwargs):

        composter_form = form_list[0]
        composter_location_form = form_list[1]
        orgName = composter_form.cleaned_data['orgName']
        email = composter_form.cleaned_data['email']
        password = composter_form.cleaned_data['password']
        composter_location = composter_location_form.cleaned_data['composter_location']
        
        composter = Composter(orgName=orgName, email=email, password=password, composter_location=composter_location)
        composter.save()
        
        return redirect('compoAccount:compoHome')


class GreenerSignView(SessionWizardView):
    form_list = [GreenerForm, GreenerLocationForm, MapForm]
    
    def get_template_names(self):
        current_step = self.steps.current
        
        template_name_map = {
            '0': 'green_sign1.html',
            '1': 'green_sign2.html',
            '2': 'green_sign3.html',
        }
        
        return [template_name_map[current_step]]
    
    def done(self, form_list, **kwargs):

        greener_form = form_list[0]
        greener_location_form = form_list[1]
        greener_map = form_list[2]

        firstName = greener_form.cleaned_data['firstName']
        lastName = greener_form.cleaned_data['lastName']
        email = greener_form.cleaned_data['email']
        password = greener_form.cleaned_data['password']
        greener_location = greener_location_form.cleaned_data['greener_location']
        
        greener = Greener(firstName=firstName,lastName=lastName, email=email, password=password, greener_location=greener_location)
        greener.save()
        
        return HttpResponse('success')