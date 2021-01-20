from __future__ import absolute_import
from celery import Celery, shared_task, current_task
from celery.exceptions import Ignore
from website.models import TwitterAccount
from django.utils import timezone
import tweepy
from website.authentication import twitter_api_auth, twitter_api_auth_using_csv
from website.network_functions import check_follower_num
import csv, json
    

def get_user_information(username):
	newAccount = TwitterAccount.objects.filter(screen_name=username)
	if len(newAccount) > 0:
		return newAccount
	else:
		api = twitter_api_auth_using_csv()
		user = api.get_user(username)
		if(user.protected):
			print("User is Private")
			return
		else:
			userId = user.id_str
			userScreenName = user.screen_name
			userDateCreated = user.created_at
			userNumFollowers = user.followers_count
			newAccount = TwitterAccount(screen_name=userScreenName,created_date=userDateCreated,follower_num=userNumFollowers) 
			newAccount.save()
			return newAccount


@shared_task
def network_rules(user_name, sender_name):
	user_account = get_user_information(user_name)
	sender_account = get_user_information(sender_name)
	print(user_account)
	print(sender_account)

	is_follower_num = check_follower_num(sender_account, 1000)

	return is_follower_num
