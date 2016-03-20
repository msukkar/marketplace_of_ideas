from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.template import loader
import requests
import json

@csrf_exempt
def home(request):
	if request.method == 'GET':
		url = 'http://exp-api:8000/experience/v1/home'
		response = requests.get(url).json()
		# Probably rearrange based on popularity, time, etc
		context = {
			'response': json.loads(response['data'])
		}
		template = loader.get_template('frontend/start.html')
		return HttpResponse(template.render(context, request))

	return JsonResponse({ 'success': False })

def post(request, post_id):
	if request.method == 'GET':
		url = 'http://exp-api:8000/experience/v1/post/' + str(post_id)
		response = requests.get(url).json()
	
		if not response['success']:
			return HttpResponse("We couldn't find a post with that id!")
		else:
			context = {
				# 'response': json.loads(response.json())
				'response': json.loads(response['data'])
			}
			template = loader.get_template('frontend/detail.html')
			return HttpResponse(template.render(context, request))

	return JsonResponse({ 'success': False })
