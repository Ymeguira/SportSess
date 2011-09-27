# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render_to_response, get_object_or_404, HttpResponseRedirect
from django.template import Context, loader
from SportSess.Events_Manager.models import Event
from django.core.urlresolvers import reverse

def index(request):
    latest_Event_list = Event.objects.all()
    return render_to_response('index.html', {'latest_Event_list': latest_Event_list})

def search(request):
    return render_to_response('search.html', )

def result(request):
    selected_event_ID = request.GET['ID']
    event = get_object_or_404(Event, pk=selected_event_ID)
    return render_to_response('detail.html', {'event': event})

def detail(request, event_id):
    event = get_object_or_404(Event, pk=event_id)
    return render_to_response('detail.html', {'event': event})

def create(request):
    return render_to_response('create.html')

def publish(request):
    return HttpResponse('Event cree')
    

    
    