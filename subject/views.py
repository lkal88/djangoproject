from django.shortcuts import render, redirect, get_object_or_404
# Create your views here.
from event.views import Event
from .models import Subject



def display(request):
    subject_list = Subject.objects.all()
    context = {
        'subject_list': subject_list
    }
    return render(request, 'subject/display.html', context)

def detail(request, subject_id):
    subject_found = get_object_or_404(Subject, pk=subject_id)
    context ={ 'subject_found': subject_found }
    return render(request, 'subject/detail.html', context)
