from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import requests

@csrf_exempt
def home(request):
	if request.method == 'GET':
		response = requests.get('http://exp-api:8000/experience/v1/home')
		# Probably rearrange based on popularity, time, etc
		return JsonResponse(response.json(), safe=False)
	return JsonResponse({ 'success': False })

def post(request, post_id):
	if request.method == 'GET':
		url = 'http://exp-api:8000/experience/v1/post/' + str(post_id)
		response = request.get(url)
		return JsonResponse(response.json(), safe=False)
	return JsonResponse({ 'success': False })
