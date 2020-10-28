from django.db import models

# Create your models here.


class TwitterAccount(models.Model):
    id = models.AutoField(primary_key=True)
    screen_name = models.TextField()