from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from xiab.apps.users.forms import UserForm

def index(request):
    return HttpResponse("Rango says hey there world!")


def register(request):
    registered = False

    if request.method == 'POST':
        # Attempt to get information from raw form data
        user_form = UserForm(data=request.POST)

        if user_form.is_valid():
            user = user_form.save()

            # Hash password with set_password and update user object
            user.set_password(user.password)
            user.save()
            registered = True
        else:
            print(user_form.errors)
    else:
        # Not a HTTP POST so render the form blank for user input
        user_form = UserForm()

    return render(request,
            'users/register.html',
            {'user_form': user_form, 'registered': registered})


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        print(request.POST)

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('/')
            else:
                return HttpResponse("Your account has been disabled.")
        else:
            # Bad login details were provided. So we can't log the user in.
            print("Invalid login details: {0}, {1}".format(username, password))
            return HttpResponse("Invalid login details supplied.")
    else:
        return render(request, 'users/login.html', {})


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/')


def profile(request):
    return render(request, 'users/profile.html')
