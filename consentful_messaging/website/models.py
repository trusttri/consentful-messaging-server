from django.db import models
from django.db.models import IntegerField, Model
##from django_mysql.models import ListTextField

# Create your models here.

class TwitterAccount(models.Model):
    id = models.AutoField(primary_key=True)
    screen_name = models.TextField()
    created_date = models.DateField(auto_now=False,auto_now_add=False)
    follower_num = models.IntegerField()
    #following_list = ListTextField(
    #    base_field=models.TextField() # list of usernames of followers of this account
    #    size = 200
    #)
    #follower_list = ListTextField( # list of usernames of accounts that this account follows
    #    base_field = models.TextField()
    #    size = 200
    #)   
    
    #constructor
    def __init__(self, id_in, username, date_made, num_followers): #list_followers, list_following):
        self.id = id_in
        self.screen_name = username
        self.created_date = date_made
        self.follower_num = num_followers

    #def addFollower(self, follower):
        
