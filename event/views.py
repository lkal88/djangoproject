from django.shortcuts import render, redirect, get_object_or_404, render_to_response
from django.http import Http404
from django.template import RequestContext
from .forms import EventCreateForm, EventUpdateForm
from .models import Event
from django.http import Http404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.views.generic import CreateView, UpdateView, DetailView, DeleteView
from django.core.exceptions import ObjectDoesNotExist

# Create your views here.
#home view
def home(request):
    event_list = Event.objects.all()
    context = {'event_list': event_list}
    return render(request, 'event/home.html', context)



#currently also allows users to post as well.
"class based views require a certain template name. e.g event_form or event_Detail"
"""
class PostCreateView(CreateView):
    model = Event
    fields = ['title', 'link', 'description', 'tags']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_success_url()
"""

@login_required
def create(request):
    if request.method == 'POST':
        form = EventCreateForm(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.author = request.user
            instance.save()
            instance.save_m2m()
            return redirect('event:home')
    else:
        form = EventCreateForm()
    return render(request, 'event/create.html', {'form': form})




class EventDetailView(DetailView):
    model = Event

""" updateview only works with eventdetailview etc.
def detail(request, event_id):
    event = get_object_or_404(Event, pk=event_id)
    return render(request, 'event/detail.html', {'event': event})
"""

class EventUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Event
    fields = ['title', 'link', 'description', 'tags']
    template_name = "event/edit.html"
    #pk_url_kwarg = 'event_id'
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        event = self.get_object()
        if self.request.user == event.author:
            return True
        return False
#class EventDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
#got to enrol and unenrol.
@login_required
def attend(request, event_id):
    event = get_object_or_404(Event, pk=event_id)
    if (event.author != request.user):
    #and (event.attendees.get(pk=request.user.id).DoesNotExist):
        #also need to check if they have already enrolled into this course.
        event.attendees.add(request.user)
        event.save()
        return render(request, 'event/attend.html', {'event': event})
    return redirect('event:detail')
"""REMOVE THE 404 STUFF LATER TO MAKE AN ITEM NOT FOUND PAGE!"""
"""if attending already, find a method to unattend. Need to work on profile next"""

def unattend(request, event_id):
    event = get_object_or_404(Event, pk=event_id)
    try:
        found = event.attendees.get(pk=request.user.id)
        found.remove()
        return render(request, 'event/unattend.html', {'event':event})
    except ObjectDoesNotExist as error:
        return redirect('event:home')
    except AttributeError as error:
        return redirect('event:home')

#delete view
#IF U GET A TYPERROR WITH UNEXPECTED ARGUMENT PK, CHANGE THE URL PATTERN TO EVENT_ID.
@login_required
def delete(request, event_id):
    try:
        event = get_object_or_404(Event, pk=event_id)
        if (event.author == request.user):
        #move to error page.
            event.delete()
        return render(request, 'event/delete.html', {'event':event})
    except ObjectDoesNotExist as error:
        return redirect('event:home')

class EventDeleteView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Event
    success_url = '/'

    def test_func(self):
        event = self.get_object()
        if self.request.user == event.author:
            return True
        return False

#if there is {% now %}
"""
def review(request, event_id):
    event = get_object_or_404(Event, pk=event_id)
    Should write a separate model for testimonials because they use user & textfield.


"""
