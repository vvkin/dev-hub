from django.contrib.auth.backends import ModelBackend
from django.contrib.auth.models import User

class EmailOrUsernameBackend(ModelBackend):
    """ 
    Class allows authentication with both username and email
    """
    def authenticate(self, request, username=None, password=None, **kwargs):
        # Determine used email or username
        if '@' in username:
            kwargs = {'email': username}
        else:
            kwargs = {'username': username}
        # Check user exists with current data
        try:
            user = User.objects.get(**kwargs)
            if user.check_password(password):
                return user
        except User.DoesNotExist:
            return None