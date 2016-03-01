from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
import requests
import json

@csrf_exempt
def home(request):
	if request.method == 'GET':
		response = requests.get('http://models-api:8000/api/v1/posts')
		# Probably rearrange based on popularity, time, etc
		response_json = response.json()
		response_jsonified = json.loads(response_json)
		for post in response_jsonified:
			author_id = str(post['fields']['author'])
			author_response = requests.get('http://models-api:8000/api/v1/users/' + author_id)
			author_response_json = json.loads(author_response.json())[0]
			post['fields']['author_name'] = author_response_json['fields']['first_name'] + ' ' + author_response_json['fields']['last_name']
		response_json = json.dumps(response_jsonified)
		return JsonResponse(response_json, safe=False)
	return JsonResponse({ 'success': False })

def post(request, post_id):
	if request.method == 'GET':
		post_url = 'http://models-api:8000/api/v1/posts/' + str(post_id)
		comments_url = 'http://models-api:8000/api/v1/comments/post/' + str(post_id)

		post_raw = requests.get(post_url)
		comments_raw = requests.get(comments_url)

		post_json = post_raw.json()
		comments_json = comments_raw.json()

		post_jsonified = json.loads(post_json)
		comments_jsonified = json.loads(comments_json)

		post_jsonified['fields']['comments'] = []
		for comment in comments_jsonified:
			post_json['fields']['comments'].append(comment)

		return JsonResponse(json.dumps(post_jsonified), safe=False)
		#return JsonResponse(response.json(), safe=False)
	return JsonResponse({ 'success': False })
