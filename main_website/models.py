from django.db import models

class Champion(models.Model):
    champion_name = models.CharField(max_length=30)
    link_to_presentation = models.URLField(max_length=200, null=True)
    champion_icon = models.ImageField(upload_to='champion/icon/')
    current_patch = models.CharField(max_length=15)
    champion_desc = models.TextField(max_length=300, null=True)


# Create your models here.
