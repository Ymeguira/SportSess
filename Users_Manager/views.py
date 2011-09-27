from django.contrib.auth import authenticate, logout as authlogout, models as authmodels
from django.contrib import auth
from SportSess.Users_Manager import models as usermodels
from django.db import models as dbmodels
from django.views.decorators.csrf import csrf_protect
from django.http import HttpResponse
from django.shortcuts import render_to_response

def logout(request):
    authlogout(request)
    return render_to_response('login.html', )
    # Redirect to a success page.
    
    
def authentication(request):
    
    logged_username = request.POST['username']
    logged_password = request.POST['password']
    
    user = authenticate(username=logged_username, password=logged_password)
    if user is not None:
        if user.is_active:
            auth.login(request, user)
            # Redirect to a success page.
            sportsessuser = user.get_profile()
            return render_to_response('home.html', {'logged_user': sportsessuser})
        else:
            # Return a 'disabled account' error message
            return HttpResponse("Compte inactif")
    else:
        # Return an 'invalid login' error message.
        return HttpResponse("Mauvais password")
    
@csrf_protect
def sign_up(request):
    
    signup_email = dbmodels.EmailField()
    
    signup_username = request.POST['username']
    signup_last_name = request.POST['last_name']
    signup_first_name = request.POST['first_name']
    signup_email = request.POST['first_email']
    signup_password = request.POST['password']
    signup_gender = request.POST['gender']
    signup_year = request.POST['year']
    signup_month = request.POST['month']
    signup_day = request.POST['day']
    
    signup_birthday = dbmodels.datetime.date(int(signup_year), int(signup_month), int(signup_day))
    
    new_user = authmodels.User(username=signup_username, last_name=signup_last_name, first_name=signup_first_name, email=signup_email, password=signup_password)
    new_user.save()
    
    new_SportSessUser = usermodels.SportSessUser(user=new_user, birthday = signup_birthday, gender=signup_gender)
    new_SportSessUser.save()

    if new_user.is_active:
        new_user.backend='django.contrib.auth.backends.ModelBackend'
        auth.login(request, new_user)
        # Redirect to a success page.
        return render_to_response('home.html', {'logged_user': new_user})
    else:
        # Return a 'disabled account' error message
        return HttpResponse("Compte inactif")

def profil(request):
    if request.user.is_authenticated():
    # Do something for authenticated users.
        sportSessUser = request.user.get_profile()
        return render_to_response('profil.html', {'logged_user': sportSessUser})
    else:
    # Do something for anonymous users.
        return HttpResponse("No user logged_in")
    

def friends_list(request):
    return HttpResponse("Friends Page")

def messages(request):
    return HttpResponse("Messages Page")
