from django.shortcuts import render
from django.views.generic import ListView
from .models import Entry

# Create your views here.

def home(request):
    context_object_name = Entry.objects.all()
    return render(request, 'entries/index.html',{"blog_entries":context_object_name})