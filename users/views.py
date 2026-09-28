from django.shortcuts import render, redirect
from django.contrib.auth import login

from .forms import SignUpForm


# define a function view called signup_view that takes a request from user
def signup_view(request):
    # when user submits the signup form, a POST request is generated
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()              # create the new user
            login(request, user)            # log them in right away
            return redirect('recipes:list')  # send them to their recipe list
    else:
        form = SignUpForm()

    context = {'form': form}
    return render(request, 'auth/signup.html', context)
