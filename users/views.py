from django.shortcuts import render, redirect
from users.forms import SignUpForm
from users.services.signup import validate_request_and_login

def signup(request):
    if request.method == 'POST':
        validate_request_and_login(request)
        return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'users/signup.html', {'form' : form})
    
