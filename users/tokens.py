from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.utils import six


class AccountActivationToken(PasswordResetTokenGenerator):
    """ 
    Token generator inherited from reset password token generator.
    Generate unique hash value for email approving
    """
    def _make_hash_value(self, user, timestamp):
        return (
            six.text_type(user.pk) + six.text_type(timestamp) + 
            six.text_type(user.profile.email_confirmed)
        )

# Create token object
account_activation_token = AccountActivationToken()
