from django.contrib import admin
from .models import G_Image

# Register your models here.
@admin.register(G_Image)
class GImageAdmin(admin.ModelAdmin):
    list_display = ['img_id', 'catagory', 'name', 'img' ]
