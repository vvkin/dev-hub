from django.db import models
from django.contrib.auth import get_user_model

class Interest(models.Model):
    """Users interests"""

    user_id = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    name = models.CharField(max_length=255)

    class Meta:
        db_table = 'user_interests'



class Follower(models.Model):
    """Model for follow/following relationship"""

    class RelationType(models.IntegerChoices):
        """Possible types of relations between users"""
    
        FOLLOWING = 0 # User A is a follower of the user B, but
        FOLLOWED =  1 # user B is followed by user A

    user_id = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    relation_type = models.IntegerField(choices=RelationType.choices)

    class Meta:
        db_table = 'user_follow_relation'


