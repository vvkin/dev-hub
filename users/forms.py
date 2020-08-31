from django import forms
from django.contrib.auth.forms import UserCreationForm
from users.models import CustomUser

class SignUpForm(UserCreationForm):
    """ Just add additonal required email field """
    email = forms.EmailField(max_length=254, help_text="Required. Valid email address")
    class Meta(UserCreationForm.Meta):
        model = CustomUser