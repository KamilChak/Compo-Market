from django.shortcuts import render, redirect
from formtools.wizard.views import SessionWizardView
from .models import Composter
from .forms import UserForm, PointForm

def welcome(request):
    return render(request, 'welcome.html')

def home(request):
    return render(request, 'home.html')

class CompoSignView(SessionWizardView):
    form_list = [UserForm, PointForm]
    
    def get_template_names(self):
        # Get the current step in the wizard
        current_step = self.steps.current
        
        # Map each step to its corresponding template
        template_name_map = {
            '0': 'compo_sign.html',
            '1': 'compo_map.html',
        }
        
        # Return the template for the current step
        return [template_name_map[current_step]]
    
    def done(self, form_list, **kwargs):
        # Get form data
        user_form = form_list[0]
        point_form = form_list[1]
        username = user_form.cleaned_data['username']
        email = user_form.cleaned_data['email']
        password = user_form.cleaned_data['password']
        point = point_form.cleaned_data['point']
        
        # Create a new Composter object
        composter = Composter(username=username, email=email, password=password, point=point)
        composter.save()
        
        return redirect('authenticate:home')
