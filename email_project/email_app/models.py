from django.db import models
from django.contrib.auth.models import User
#from social_django.models import UserSocialAuth


""""class UserSocialAuthModel(models.Model):
    # user = models.OneToOneField(User, on_delete=models.CASCADE)
    provider = models.CharField(max_length=255)
    uid = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.provider}"""
