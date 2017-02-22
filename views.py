from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect,HttpResponse
from django.urls import reverse
from django.views import generic
from django.utils import timezone

def show_home(request):
    return render(request, 'homepage/homepage.html')
    
