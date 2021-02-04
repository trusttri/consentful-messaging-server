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


