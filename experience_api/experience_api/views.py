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
		response_jsonified = json.loads(response_json['response'])
		for post in response_jsonified:
			author_id = post['fields']['author']
			author_response = requests.get('http://models-api:8000/api/v1/users/' + str(author_id))
			author_response_json = json.loads(author_response.json()['response'])[0]
			post['fields']['author_name'] = author_response_json['fields']['first_name'] + ' ' + author_response_json['fields']['last_name']
		response_json = json.dumps(response_jsonified)
		return JsonResponse({ 'success': True, 'data': response_json }, safe=False)
	return JsonResponse({ 'success': False })

def post(request, post_id):
	if request.method == 'GET':
		url = 'http://models-api:8000/api/v1/posts/' + str(post_id)
		response = requests.get(url)

		response_json = response.json()

		if response_json['success']:
			posts_json = json.loads(response_json['response'])
			for post in posts_json:
				author_id = post['fields']['author']
				author_response = requests.get('http://models-api:8000/api/v1/users/' + str(author_id))
				author_response_json = json.loads(author_response.json()['response'])[0]
				post['fields']['author_name'] = author_response_json['fields']['first_name'] + ' ' + author_response_json['fields']['last_name']

				post_id = post['pk']
				comments = requests.get('http://models-api:8000/api/v1/comments?post_id=' + str(post_id))
				comments_object = json.loads(comments.json())
				for comment in comments_object:
					author_id = comment['fields']['author']
					author_response = requests.get('http://models-api:8000/api/v1/users/' + str(author_id))
					author_response_json = json.loads(author_response.json()['response'])[0]
					comment['fields']['author_name'] = author_response_json['fields']['first_name'] + ' ' + author_response_json['fields']['last_name']
				post['fields']['comments'] = comments_object
			return JsonResponse({ 'success': True, 'data': json.dumps(posts_json)})
		#return JsonResponse(response.json(), safe=False)
	return JsonResponse({ 'success': False, 'response': 'No post with specified id' })

@csrf_exempt
def new_post(request):
	if request.method == 'POST':
		url = 'http://models-api:8000/api/v1/posts/new'

		response = requests.post(
			url,
			data = {
				'authenticator': request.POST['authenticator'],
				'title': request.POST['title'],
				'body': request.POST['body'],
			},
		)

		if response and response.json()['success']:
			return JsonResponse({ 'success': True, 'response': 'Successfully added a new post' })
		else:
			return HttpResponse(response.json()['response'])

@csrf_exempt
def sign_in(request):
	if request.method == 'POST':
		url = 'http://models-api:8000/api/v1/users/sign_in'
		response = requests.post(
			url,
			data = {
				'username': request.POST['username'],
				'password': request.POST['password'],
			},
		)
		if response and response.json()['success']:
			return JsonResponse({ 'success': True, 'response': response.json()['authenticator']})
		else:
			return HttpResponse(response.json()['response'])

@csrf_exempt
def sign_up(request):
	if request.method == 'POST':
		url = 'http://models-api:8000/api/v1/users/new'
		response = requests.post(
			url,
			data = {
				'username': request.POST['username'],
				'first_name': request.POST['first_name'],
				'last_name':request.POST['last_name'],
				'password': request.POST['password'],
			},
		)

		if response and response.json()['success']:
			return JsonResponse({ 'success': True, 'response': 'ok'})
		else:
			return HttpResponse(response)

@csrf_exempt
def sign_out(request):
	if request.method == 'POST':
		url = 'http://models-api:8000/api/v1/users/sign_out'
		response = requests.post(
			url,
			data = {
				'authenticator': request.POST['authenticator'],
			},
		)

		if response and response.json()['success']:
			return JsonResponse({ 'success': True, 'response': 'Authenticator deleted' })
		else:
			return JsonResponse({ 'success': False, 'response': response.json()['response'] })