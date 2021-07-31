from django.db import models


# Create your models here.

class Member(models.Model):
    memeber_id = models.AutoField(primary_key=True)
    member_name = models.CharField(max_length=20)
    member_email = models.EmailField(max_length=50)
    member_contact = models.CharField(max_length=13)

    def __str__(self):
        return self.member_name
