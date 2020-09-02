from django.shortcuts import render, redirect
from django.views import generic
from users.forms import SignUpForm
from users.services.signup import validate_request_and_login


def signUp(request):
    """Functional view for sign up users"""
    if request.method == 'POST':
        validate_request_and_login(request)
        return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'users/signup.html', {'form' : form})

def activate(request):
    """Function view for account activation"""
    

class AccountActivationSent(generic.TemplateView):
    template_name = 'users/activation_sent.html'

    
