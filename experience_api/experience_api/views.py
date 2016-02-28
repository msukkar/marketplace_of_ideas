from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import requests

@csrf_exempt
def home(request):
	if request.method == 'GET':
		response = requests.get('http://localhost:8001/api/v1/posts')
		# Probably rearrange based on popularity, time, etc
		return JsonResponse(response.json())
	return JsonResponse({ 'success': False })

def post(request, post_id):
	if request.method == 'GET':
		url = 'http://localhost:8001/api/v1/posts/' + str(post_id)
		response = request.get(url)
		return JsonResponse(response.json())
	return JsonResponse({ 'success': False })