from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
import requests

@csrf_exempt
def home(request):
	if request.method == 'GET':
		response = requests.get('http://models-api:8000/api/v1/posts')
		# Probably rearrange based on popularity, time, etc
		return JsonResponse(response.json(), safe=False)
	return JsonResponse({ 'success': False })

def post(request, post_id):
	if request.method == 'GET':
		url = 'http://model-api:8000/api/v1/posts/' + str(post_id)
		response = requests.get(url)
		return HttpResponse(response.text)
		#return JsonResponse(response.json(), safe=False)
	return JsonResponse({ 'success': False })
