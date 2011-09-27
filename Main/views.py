# Create your views here.
from django.shortcuts import render_to_response
from django.http import HttpResponse


def login(request):
    if request.user.is_authenticated():
    # Do something for authenticated users.
        sportSessUser = request.user.get_profile()
        return render_to_response('home.html', {'logged_user': sportSessUser})
    else:
    # Do something for anonymous users.
        return render_to_response('login.html', )

def home(request):
    if request.user.is_authenticated():
    # Do something for authenticated users.
        sportSessUser = request.user.get_profile()
        return render_to_response('home.html', {'logged_user': sportSessUser})
    else:
    # Do something for anonymous users.
        return render_to_response('login.html', )
    
