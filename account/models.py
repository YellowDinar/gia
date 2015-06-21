# -*- coding: utf-8 -*-
from django.contrib.auth.models import User
from django.db import models


class UserProfile(models.Model):
    # This line is required. Links UserProfile to a User model instance.
    user = models.OneToOneField(User,
                                related_name='profile',
                                verbose_name=(u'Пользователь'),
                                primary_key=True
                                )

    # The additional attributes we wish to include.
    school = models.CharField(u'Школа', max_length=30)
    result = models.CharField(max_length=4, null=True)


# Override the __unicode__() method to return out something meaningful!
def __unicode__(self):
    return self.user.username