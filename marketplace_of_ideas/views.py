from django.http import JsonResponse
from django.core import serializers
from marketplace_of_ideas.models import *
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def users(request):
    if request.method == 'GET':
        return JsonResponse(serializers.serialize('json', User.objects.all()), safe=False)
    elif request.method == 'POST':
        user = User(username=request.POST["username"], first_name=request.POST["first_name"], last_name=request.POST["last_name"], password=request.POST["password"])
        user.save()
        return JsonResponse({ "success": True })

@csrf_exempt
def transactions(request):
    if request.method == 'GET':
        return JsonResponse(serializers.serialize('json', Transaction.objects.all()), safe=False)
    elif request.method == 'POST':
        transaction = Transaction(payer_id=request.POST["payer_id"], receiver_id=request.POST["receiver_id"], blog_post_id=request.POST["blog_post_id"], amount=request.POST["amount"])
        transaction.save()
        return JsonResponse({ "success": True })

@csrf_exempt
def posts(request):
    if request.method == 'GET':
        return JsonResponse(serializers.serialize('json', BlogPost.objects.all()), safe=False)
    elif request.method == 'POST':
        post = BlogPost(title=request.POST["title"], body=request.POST["body"], author_id=request.POST["author_id"])
        post.save()
        return JsonResponse({ "success": True })

@csrf_exempt
def comments(request):
    if request.method == 'GET':
        return JsonResponse(serializers.serialize('json', Comment.objects.all()), safe=False)
    elif request.method == 'POST':
        comment = Comment(blog_post_id=request.POST["blog_post_id"], author_id=request.POST["author_id"], text=request.POST["text"])
        comment.save()
        return JsonResponse({ "success": True })

def test(request):
    return JsonResponse({ "success": True })