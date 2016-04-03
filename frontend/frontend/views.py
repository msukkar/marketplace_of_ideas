from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.template import loader
from django.core.urlresolvers import reverse
import requests
import json
from .forms import LoginForm, BlogPostForm, SignupForm

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


# def create_listing(request):
#     auth = request.COOKIES.get('auth')
#     if not auth:
#       # handle user not logged in while trying to create a listing
#       return HttpResponseRedirect(reverse("login") + "?next=" + reverse("create_listing")
#     if request.method == 'GET':
#       return render("create_listing.html", ...)
#     f = create_listing_form(request.POST)
#     ...
#     resp = create_listing_exp_api(auth, ...)
#     if resp and not resp['ok']:
#         if resp['error'] == exp_srvc_errors.E_UNKNOWN_AUTH:
#             # exp service reports invalid authenticator -- treat like user not logged in
#             return HttpResponseRedirect(reverse("login") + "?next=" + reverse("create_listing")
#      ...
#      return render("create_listing_success.html", ...)
def new_blogpost(request):
	auth = request.COOKIES.get('auth')
	if not auth:
		return HttpResponseRedirect(reverse("login") + "?next=" + reverse("new_blogpost"))
	if request.method == 'POST':
		form = BlogPostForm(request.POST)

		if form.is_valid():
			title = form.cleaned_data['title']
			body = form.cleaned_data['body']

			response = requests.post(
				'http://exp-api:8000/experience/v1/post/new',
				data = {
					'title': title,
					'body': body,
					'authenticator': auth,
				}
			)

			if response and response.json()['success']:
				return HttpResponseRedirect(reverse('home'))
			elif not response.json()['success']:
				return HttpResponseRedirect(reverse("login") + "?next=" + reverse("create_listing"))
			return HttpResponse("You submitted data" + title + " " + body)

	else:
		form = BlogPostForm()

	return render(request, 'frontend/new_blogpost.html', {'form': form})

def login(request):
	blank_form = LoginForm()
	if request.method == 'GET':
	  next = request.GET.get('next') or reverse('home')
	  return render(request, 'frontend/login.html', {'next': next, 'form': blank_form})
	f = LoginForm(request.POST)
	if not f.is_valid():
	  error = 'invalid entry'
	  # bogus form post, send them back to login page and show them an error
	  return render(request, 'frontend/login.html', {'error':error, 'form':blank_form})
	username = f.cleaned_data['username']
	password = f.cleaned_data['password']
	next = f.cleaned_data.get('next') or reverse('home')
	resp = requests.post(
		'http://exp-api:8000/experience/v1/sign_in',
		data = {
			'username': username,
			'password': password,
		}
	) 
	if not resp or not resp.json()['success']:
	  error = "invalid login credentials"
	  # couldn't log them in, send them back to login page with error
	  return render(request, 'frontend/login.html', {'error':error, 'form':blank_form})
	# logged them in. set their login cookie and redirect to back to wherever they came from
	authenticator = resp.json()['response']
	response = HttpResponseRedirect(next)
	response.set_cookie('auth', authenticator)
	return response

def signup(request):
	blank_form = SignupForm()
	if request.method == 'GET':
		return render (request, 'frontend/signup.html', {'form': blank_form})
	f = SignupForm(request.POST)
	if not f.is_valid():
		error = 'invalid entry'
		return render(request, 'frontend/signup.html', {'error':error, 'form':blank_form})
	username = f.cleaned_data['username']
	password = f.cleaned_data['password']
	first_name = f.cleaned_data['first_name']
	last_name = f.cleaned_data['last_name']
	resp = requests.post(
		'http://exp-api:8000/experience/v1/sign_up',
		data = {
			'username': username,
			'first_name': first_name,
			'last_name': last_name,
			'password': password,
		}
	) 

	if not resp or not resp.json()['success']:
		error = "couldn't create account"
		return HttpResponseRedirect(reverse('login'))
	response = HttpResponseRedirect('login')
	return response

def signout(request):
	auth = request.COOKIES.get('auth')
	if not auth:
		return HttpResponseRedirect(reverse("login") + "?next=" + reverse("new_blogpost"))
	if request.method == 'GET':
		
		resp = requests.post(
			'http://exp-api:8000/experience/v1/sign_out',
			data = {
				'authenticator': auth,
			}
		)

		if not resp or not resp.json()['success']:
			error = 'couldn\'t sign out'
			response = HttpResponseRedirect(reverse('home'))
			response.delete_cookie('auth')
			auth = request.COOKIES.get('auth')
			return response
		else:
			response = HttpResponseRedirect(reverse('home'))
			response.delete_cookie('auth')
			return response

def results(request):
	if request.method == 'POST':

		if request.POST.get('query'):
			query_text = request.POST['query']
			# return HttpResponse(query_text)

			response = requests.post(
				'http://exp-api:8000/experience/v1/search',
				data = {
					'query': query_text,
				}
			)

			if response and response.json()['success']:
				# return HttpResponse(response.json()['response']['hits']['hits'])
				return render(request, 'frontend/search_results.html', {'results': response.json()['response']})
				# return HttpResponseRedirect(reverse(''))
			elif not response.json()['success']:
				return HttpResponseRedirect(reverse("login") + "?next=" + reverse("create_listing"))





