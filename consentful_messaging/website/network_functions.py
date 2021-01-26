import tweepy
from website.models import TwitterAccount
from website.authentication import twitter_api_auth, twitter_api_auth_using_csv

def check_follower_num(sender, threshold):
	'''
	checks whether sender is None for now because we haven't written code 
	to cover cases when the sender's account is private in get_user_information (a function in tasks.py)
	(it causes an error which makes sender a None)
	'''
	if sender!= None and sender.follower_num > threshold:
		return True
	else:
		return False

###### time consuming functions ######
def check_follow(user, sender):
	api = twitter_api_auth_using_csv()
	friendship = api.show_friendship(source_screen_name=user.screen_name, target_screen_name=sender.screen_name)
	print(friendship[0])
	if friendship[0].following == True:
		return True
	else:
		return False

def check_mutuals(user, sender):
	return False

# Check if user has liked sender's tweet before
def check_like_history(user, sender):
	return False

# Check if user's following has blocked sender
def check_mutual_block(user, sender):
	return False

# Check if user's mutuals have liked sender's tweet before
def check_mutual_like_history(user, sender):
	return False

# Check if user's mutuals have retweeted sender's tweets before
def check_mutual_retweet_history(user, sender):
	return False

# Check if user has ever messaged the sender
def check_message_history(user, sender):
	return False

