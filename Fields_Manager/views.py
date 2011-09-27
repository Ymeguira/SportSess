# Create your views here.
from django.http import HttpResponse

def fields_index(request):
    return HttpResponse("Fields Index Page")