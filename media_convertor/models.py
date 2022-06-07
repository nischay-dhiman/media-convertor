from django.db import models

# Create your models here.
from django.db import models



class Document(models.Model):
    mediaFile = models.FileField(upload_to='documents/')
