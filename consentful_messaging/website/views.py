from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse, JsonResponse
# Create your views here.
def index(request):
	template = loader.get_template('website/index.html')
	context = {}
	return HttpResponse(template.render(context, request))

def author_network_rules(request):
	return False
	
