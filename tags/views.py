from django.shortcuts import render
from django.shortcuts import render, redirect, get_object_or_404
from event.views import Event
from .models import Tags

# Create your views here.


def display(request):
    tag_list = Tags.objects.all()
    context = {
        'tag_list': tag_list
    }
    return render(request, 'tags/display.html', context)

def detail(request, tag_id):
    tag_found = get_object_or_404(Tags, pk=tag_id)
    context ={ 'tag_found': tag_found}
    return render(request, 'tags/detail.html', context)


"""
def detail(request, event_id):
    event = get_object_or_404(Event, pk=event_id)
    return render(request, 'event/detail.html', {'event': event})
"""
"""""
    tag = get_object_or_404(Tags, pk=tag_id)
    tag_list = tag.objects.all()
    context = {
        'tag': tag,
        'tag_list': tag_list
    }
    return render(request, 'tags/display.html', context )
"""
