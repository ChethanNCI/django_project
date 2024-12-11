'''
This will import render and redirect from shortcuts
'''
from django.shortcuts import render

def dashboard(request):
    ''' This will renturn the dashboard.html page '''
    return render(request, 'dashboard/dashboard.html')
    