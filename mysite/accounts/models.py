from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Member(models.Model):
    memeber_id = models.AutoField(primary_key=True)
    member_name = models.CharField(max_length=20)
    member_email = models.EmailField(max_length=50)
    member_contact = models.CharField(max_length=13)

    def __str__(self):
        return self.member_name

GENDER = [
    ('M','Male'), 
    ('F','Female'),
    ]

class UserMembers(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    user_name = models.CharField(max_length=20)
    user_email = models.EmailField(max_length=50)
    user_gender = models.CharField(max_length=10, choices=GENDER)
    user_desc = models.TextField(max_length=100)

    def __str__(self):
        return self.user_name
