from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    """User model that may be extended"""
    pass

class Profile(models.Model):
    """
    General information about user.
    Basic auth User model is used in many cases, so
    it will be better to save additional information, that
    can be large in another table
    """

    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    work_position = models.CharField(max_length=100, blank=True)
    location = models.CharField(max_length=50, blank=True)
    profile_image = models.ImageField(blank=True)
    posts_amount = models.PositiveIntegerField(default=0)
    comments_amount = models.PositiveIntegerField(default=0)
    followers_amount = models.PositiveIntegerField(default=0)
    following_amount = models.PositiveIntegerField(default=0)

    class Meta:
        db_table = 'user_profile'


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
