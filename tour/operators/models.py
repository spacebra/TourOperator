from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.db import models

class UserProfileManager(models.Manager):

    def create_user_profile(self, email, first_name, last_name, password):
        username = generate_md5_base64(email)
        user = User.objects.create_user(username, '', password)

        return UserProfile.objects.create(user=user, email=email, first_name=first_name, last_name=last_name)

    def remove_user(self, user):
        user.get_profile().delete()
        user.delete()

class Operator(models.Model):
    user = models.OneToOneField(User)
    email = models.EmailField(max_length=254) # use this field as username to login
    first_name = models.CharField(max_length=100) # first_name and last_name in contrib.auth.User is too short
    last_name = models.CharField(max_length=100)

    objects = UserProfileManager()
