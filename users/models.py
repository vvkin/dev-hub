from django.db import models
from django.contrib.auth import get_user_model


class PublicInformation(models.Model):
    """Public information about user"""

    user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE,
        help_text="Primary key of user that holds current information"
    )
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

    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE,
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

    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    relation_type = models.IntegerField(choices=RelationType.choices)

    class Meta:
        db_table = 'user_follow_relation'
