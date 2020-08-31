from django.conf import settings
from django.contrib.auth import authenticate, login
from django.dispatch import receiver
from django.db.models.signals import post_save
from users.models import Profile
from users.forms import SignUpForm


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_user_profile(sender, instance, created, **kwargs):
    """Create user Profile if it doesn't exist and save"""
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()

def validate_request_and_login(request):
    """ Retrieve data from request and login """
    data = request.POST
    form = SignUpForm(data)
    if form.is_valid():
        form.save()
        username = form.cleaned_data.get('username')
        raw_password = form.cleaned_data.get('password1') # or password2
        user = authenticate(username=username, password=raw_password)
        login(request, user)



