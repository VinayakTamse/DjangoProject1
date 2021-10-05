from django.db import models

# Create your models here.

class G_Image(models.Model):
    img_id = models.AutoField(primary_key=True)
    catagory = models.CharField(max_length=50)
    name = models.CharField(max_length=20)
    img = models.ImageField(upload_to='index/images/')

