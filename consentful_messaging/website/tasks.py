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
		return newAccount[0]
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
			userProtected = user.protected
			userFollowingNum = user.friends_count
			newAccount = TwitterAccount(screen_name=userScreenName,created_date=userDateCreated,follower_num=userNumFollowers,twitter_id=userId,protected=userProtected, following_num=userFollowingNum) 
			#need to get suspended info 

			getFollowers(api,newAccount)
			getFollowing(api,newAccount)

			newAccount.save()
			return newAccount

def getFollowers(api, twitter_account):
	#getting all followers: followers.ids() seems to return all id's, not sure if there is a max
	follower_list = api.followers_ids(twitter_account.screen_name)
	for follower in follower_list:
		followerAccount = TwitterAccount(twitter_id=follower)
		twitter_account.followers.add(followerAccount)

def getFollowing(api, twitter_account):
	#getting all following -- friends.ids() returns a lot of id's, not sure what the max is
	following_list = api.friends_ids(twitter_account.screen_name)
	for follow in following_list:
		followAccount = TwitterAccount(twitter_id=follow)
		twitter_account.following.add(followAccount)



@shared_task
def network_rules(user_name, sender_name):
	user_account = get_user_information(user_name)
	sender_account = get_user_information(sender_name)
	print(user_account)
	print(sender_account)

	is_follower_num = check_follower_num(sender_account, 1000)

	return is_follower_num
