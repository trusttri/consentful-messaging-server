from django.db import models
from django.db.models import IntegerField, Model
##from django_mysql.models import ListTextField

# Create your models here.

class TwitterAccount(models.Model):
  id = models.AutoField(primary_key=True)
  screen_name = models.TextField()
  created_date = models.DateField(auto_now=False,auto_now_add=False)
  follower_num = models.IntegerField()
  followers = models.ManyToManyField("self", symmetrical=False, related_name="following")