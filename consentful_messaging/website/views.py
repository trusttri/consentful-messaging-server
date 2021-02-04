from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
import os
import tweepy
from website.models import TwitterAccount
from website.tasks import network_rules


def index(request):
	template = loader.get_template('website/index.html')
	context = {}
	return HttpResponse(template.render(context, request))


@csrf_exempt
def author_network_rules(request):
<<<<<<< HEAD
	user_name = request.GET.get('user')
	sender_name = request.GET.get('sender')

	task = network_rules.delay(user_name, sender_name)

	request.session['task_id'] = task.id

	data = {'user': user_name, 'sender': sender_name, 
			'state': task.status,
			'task_id': task.id}
	
	json_data = json.dumps(data)
	response = HttpResponse(json_data, content_type='application/json')
	response["Access-Control-Allow-Origin"] = "*"
	response["Access-Control-Allow-Methods"] = "POST, GET, OPTIONS, PUT, DELETE, HEAD"
	response["Access-Control-Max-Age"] = "1000"
	response["Access-Control-Allow-Headers"] = "X-Requested-With, Content-Type"
	print(response)
	return response


@csrf_exempt
def poll_status(request):
	task_id = request.GET.get('task_id')

	task = network_rules.AsyncResult(task_id)
	data = {
			'task_id': task_id,
			'state': task.state,
			}

	if task.state == "SUCCESS":
		data['state'] = 'SUCCESS'
		data['result'] = task.get()
	elif task.state == "PENDING" or task.state == "RECEIVED" or task.state == "STARTED":
		data['state'] = "PENDING"
		data['result'] = "PENDING"
=======
  user = request.GET.get('user')
  sender = request.GET.get('sender')
  print(user, sender)

  # return placeholder response for now
  data = {'response': 'True'}
  json_data = json.dumps(data)
  response = HttpResponse(json_data, content_type='application/json')
  response["Access-Control-Allow-Origin"] = "*"
  response["Access-Control-Allow-Methods"] = "POST, GET, OPTIONS, PUT, DELETE, HEAD"
  response["Access-Control-Max-Age"] = "1000"
  response["Access-Control-Allow-Headers"] = "X-Requested-With, Content-Type"
  print(response)
  return response

# helper function for API key authentication
def twitter_api_auth(consumer_key, consumer_secret, acc_key, acc_secret):
  auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
  auth.set_access_token(acc_key, acc_secret)
  api = tweepy.API(auth, wait_on_rate_limit=True)
  try:
  	api.verify_credentials()
  	print("Authentication OK")
  except:
  	print("Error during authentication")
  return api
    
# API key authentication
def twitter_api_auth_using_csv():
	import os
	workpath = os.path.dirname(os.path.abspath(__file__))
	with open(os.path.join(workpath, 'twitter-creds.csv'), 'rt') as csv_file:
		reader = csv.DictReader(csv_file, delimiter=',')
		for row in reader:
			consumer_key = row['consumer_key']
			consumer_secret = row['consumer_secret']
			acc_key = row['access_key']
			acc_secret = row['access_secret']
		try:
			return twitter_api_auth(consumer_key, consumer_secret, acc_key, acc_secret)
		except NameError:
			raise RuntimeError("Check if you have Twitter API keys in the csv file.")

def get_user_information(username):
	api = twitter_api_auth_using_csv()
	user = api.get_user(username)
	if(user.protected):
		print("User is Private")
		return
>>>>>>> b80884d... separate file temp
	else:
		data['state'] = "FAILURE"
		data['result'] = "FAILURE"


	json_data = json.dumps(data)
	response = HttpResponse(json_data, content_type='application/json')
	response["Access-Control-Allow-Origin"] = "*"
	response["Access-Control-Allow-Methods"] = "POST, GET, OPTIONS, PUT, DELETE, HEAD"
	response["Access-Control-Max-Age"] = "1000"
	response["Access-Control-Allow-Headers"] = "X-Requested-With, Content-Type"
	print(response)
	return response




def get_user_200_tweets(username):
	api = twitter_api_auth_using_csv()
	try:
		statuses = api.user_timeline(screen_name = username,count=200, tweet_mode="extended")
	except tweepy.TweepError as e:
		return 'Not authorized.'
			
	tweet_info = {}

	for tweet in statuses:
		if hasattr(tweet, 'retweeted_status'):
			tweet_info[tweet.id] = {'text': tweet.retweeted_status.full_text, 'tweet_time': tweet.created_at,
			'urls': extract_urls(tweet.retweeted_status)}
		else:
			tweet_info[tweet.id] = {'text': tweet.full_text, 'tweet_time': tweet.created_at,
			'urls': extract_urls(tweet)}
	return tweet_info

