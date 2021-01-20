import tweepy
from website.models import TwitterAccount

def check_follower_num(sender, threshold):
	if sender.follower_num > threshold:
		return True
	return False

def check_follow(user, sender):
	return False

def check_mutuals(user, sender):
	return False

def check_tweet_history(user, sender):
	return False

def check_message_history(user, sender):
	return False

def check_like_history(user, sender):
	return False

def check_mutual_block(user, sender):
	return False


