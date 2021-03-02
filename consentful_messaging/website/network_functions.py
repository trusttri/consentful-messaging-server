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

def check_mutuals(user_name, sender_name):
    api = twitter_api_auth_using_csv()
    
    user = api.get_user(user_name)
    numUserFollowing = user.friends_count
    user_following_ids = []

    users = tweepy.Cursor(api.friends_ids, screen_name=user_name)
    for page in users.pages():
        user_following_ids.extend(page)
    print("Are the list of user's following complete? " + str(len(user_following_ids) == numUserFollowing) + ", " + str(len(user_following_ids)))
    
    sender = api.get_user(sender_name)
    numSenderFollowing = sender.friends_count
    sender_following_ids = []
    senders = tweepy.Cursor(api.friends_ids, screen_name=sender_name)
    for page in senders.pages():
        sender_following_ids.extend(page)
    print("Are the list of sender's following complete?" +str(len(sender_following_ids) == numSenderFollowing) + ", " + str(len(sender_following_ids)))

    userSet = set(user_following_ids)
    senderSet = set(sender_following_ids)

    intersection = userSet.intersection(senderSet)
    if len(intersection) > 0:
        return True
    else:
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

# Returns a user's recent 200 likes
def return_recent_likes(username):
    api = twitter_api_auth_using_csv()
    try:
        liked_list = api.favorites(screen_name = username, count = 200)
    except tweepy.TweepError as e:
        return 'Not authorized.'
    return liked_list
