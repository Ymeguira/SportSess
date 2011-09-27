# Create your views here.
from django.shortcuts import render_to_response
from django.http import HttpResponse
# Create your views here.


def messages_index(request):
    if request.user.is_authenticated():
    # Do something for authenticated users.
        sportSessUser = request.user.get_profile()
        return render_to_response('messages_index.html', {'logged_user': sportSessUser})
    else:
    # Do something for anonymous users.
        return render_to_response('login.html', )
    
    
def compose(request):
    if request.user.is_authenticated():
    # Do something for authenticated users.
        sportSessUser = request.user.get_profile()
        return render_to_response('compose_message.html', {'logged_user': sportSessUser})
    else:
    # Do something for anonymous users.
        return render_to_response('login.html', )
    

def send(request):
    if request.user.is_authenticated():
    # Do something for authenticated users.
        sportSessUser = request.user.get_profile()
    
    receiver = request.POST['receiver']
    message_object = request.POST['message_object']
    message = request.POST['message']
    
    
    
    return HttpResponse("Message envoye")

def save(request):
    return HttpResponse("Message sauvegarde")
    
def delete(request):
    return HttpResponse("Message supprime")
    