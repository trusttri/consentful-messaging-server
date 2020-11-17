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
    
def key_auth_helper(consumerkey, consumersecret, token, tokensecret):
    auth = tweepy.OAuthHandler(consumerkey, consumersecret)
    auth.set_access_token(token, tokensecret)
    return auth
    
def key_auth(
    

	
