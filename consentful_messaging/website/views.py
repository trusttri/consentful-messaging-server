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
    return HttpResponse("false")
    
# helper function for authenticating API keys
def twitter_api_auth(consumer_key, consumer_secret, acc_key, acc_secret):
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(acc_key, acc_secret)
    api = tweepy.API(auth, wait_on_rate_limit=True)
    return api
    
# API key authentication
def twitter_api_auth_using_csv():
   with open('twitter-creds.csv') as csv_file
      reader = csv.reader(csv_file, delimiter=',')
      for row in reader:
         consumer_key = row['consumer_key']
         consumer_secret = row['consumer_secret']
         acc_key = row['access_key']
         acc_secret = row['access_secret']
         twitter_api_auth(consumer_key, consumer_secret, acc_key, acc_secret)
         
         
         
      
   
   
    

	
