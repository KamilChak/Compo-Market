from django.shortcuts import render

def compoHome(request):
    return render(request, 'compoHome.html')