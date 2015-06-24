# -*- coding: utf-8 -*-
from django.contrib.auth.models import User
from django.db import models


class UserProfile(models.Model):
    # This line is required. Links UserProfile to a User model instance.
    user = models.OneToOneField(User, related_name='profile', verbose_name=u'Пользователь', primary_key=True)
    result = models.IntegerField(null=True)


# Override the __unicode__() method to return out something meaningful!
def __unicode__(self):
    return self.user.username