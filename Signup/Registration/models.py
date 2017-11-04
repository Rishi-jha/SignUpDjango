# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class RegistrationTable(models.Model):
    first_name=models.CharField(max_length=20)
    last_name=models.CharField(max_length=20)
    email_id=models.CharField(max_length=50, primary_key=True)
    user_name=models.CharField(max_length=30)
    password=models.CharField(max_length=128)
    phone_num=models.IntegerField()
    
    def __str__(self):
        return self.user_name    
