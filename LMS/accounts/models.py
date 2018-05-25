from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    """
    User Profile model
    This model extends the user model provided by django auth
    """

    objects = models.Manager()

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)


