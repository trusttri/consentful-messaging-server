from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse, JsonResponse
import tweepy

def index(request):
	template = loader.get_template('website/index.html')
	context = {}
	return HttpResponse(template.render(context, request))

def author_network_rules(request):
    user = request.GET.get('user')
    sender = request.GET.get('sender')
    return HttpResponse("false")
    
def twitter_auth(consumerkey, consumersecret, token, tokensecret):
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_key, access_secret)
    return auth
    
    
	
