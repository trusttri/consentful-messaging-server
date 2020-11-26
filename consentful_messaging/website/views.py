from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse, JsonResponse
import tweepy
import csv

def index(request):
	template = loader.get_template('website/index.html')
	context = {}
	return HttpResponse(template.render(context, request))

def author_network_rules(request):
    user = request.GET.get('user')
    sender = request.GET.get('sender')

    api = twitter_api_auth_using_csv()
    print(api)
    return HttpResponse("false")
    
# helper function for authenticating API keys
def twitter_api_auth(consumer_key, consumer_secret, acc_key, acc_secret):
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(acc_key, acc_secret)
    api = tweepy.API(auth, wait_on_rate_limit=True)
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

