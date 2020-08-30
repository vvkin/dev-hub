from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    """User model that may be extended"""
    pass

class PublicInformation(models.Model):
    """
    Public information about user.
    Basic auth User model is used in many cases, so
    it will be better to save additional information, that
    can be large in another table
    """

    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    about_info = models.TextField(null=True, help_text="Information about user")
    profile_image = models.ImageField()
    posts_amount = models.PositiveIntegerField(default=0,
        help_text="Total amount of posts written by current user"
    )
    comments_amount = models.PositiveIntegerField(default=0,
        help_text="Total amount of comments written by current user"
    )
    followers_amount = models.PositiveIntegerField(default=0,
        help_text="Total amount of user followers"
    )
    following_amount = models.PositiveIntegerField(default=0,
        help_text="Total amount of users those followed by current user"
    )

    class Meta:
        db_table = 'user_public_info'


class Interest(models.Model):
    """Users interests"""

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,
        related_name="user_interests"
    )
    name = models.CharField(max_length=255)

    class Meta:
        db_table = 'user_interests'


class Follower(models.Model):
    """Model for follow/following relationship"""

    class RelationType(models.IntegerChoices):
        """Possible types of relations between users"""
        FOLLOWING = 0 # User A is a follower of the user B, but
        FOLLOWED =  1 # user B is followed by user A

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    relation_type = models.IntegerField(choices=RelationType.choices)

    class Meta:
        db_table = 'user_follow_relation'
