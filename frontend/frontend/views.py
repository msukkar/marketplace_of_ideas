from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.template import loader
import requests

@csrf_exempt
def home(request):
	if request.method == 'GET':
		response = requests.get('http://exp-api:8000/experience/v1/home')
		# Probably rearrange based on popularity, time, etc
		#return JsonResponse(response.json(), safe=False)
		context = {
			'response': response.json()
		}
		template = loader.get_template('start.html')
		return HttpResponse(template.render(context, request))

	return JsonResponse({ 'success': False })

def post(request, post_id):
	if request.method == 'GET':
		url = 'http://exp-api:8000/experience/v1/post/' + str(post_id)
		response = request.get(url)
		return JsonResponse(response.json(), safe=False)
	return JsonResponse({ 'success': False })
