from django.shortcuts import render
from django.http import HttpResponse
from xiab.apps.users.forms import UserForm, UserProfileForm

def index(request):
    return HttpResponse("Rango says hey there world!")

def register(request):
    registered = False

    if request.method == 'POST':
        # Attempt to get information from raw form data
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()

            # Hash password with set_password and update user object
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user

            if 'picture' in request.FILES:
                profile.picture = request.FILES['picture']

            profile.save()
            registered = True
        else:
            print(user_form.errors, profile_form.errors)
    else:
        # Not a HTTP POST so render the form blank for user input
        user_form = UserForm()
        profile_form = UserProfileForm()

    return render(request,
            'users/register.html',
            {'user_form': user_form, 'profile_form': profile_form, 'registered': registered})






