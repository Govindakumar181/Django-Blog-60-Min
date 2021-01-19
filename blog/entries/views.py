from django.shortcuts import render
from django.views.generic import ListView
from .models import Entry

# Create your views here.

def home(request):
    return render(request, 'entries/index.html')