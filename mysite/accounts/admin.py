from django.contrib import admin
from accounts.models import Member, UserMembers

# Register your models here.

admin.site.register([Member, UserMembers])
