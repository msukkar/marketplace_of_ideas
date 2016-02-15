from django.http import JsonResponse
from django.core import serializers
from marketplace_of_ideas.models import *
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def users(request, user_id=-1):
    if request.method == 'GET':
        if user_id == -1:
            return JsonResponse(serializers.serialize('json', User.objects.all()), safe=False)
        else:
            try:
                user = User.objects.get(pk=user_id)
                return JsonResponse(serializers.serialize('json', user), safe=False)
            except User.DoesNotExist:
                return JsonResponse({ 'success': False})
    elif request.method == 'POST':
        user = User(username=request.POST["username"], first_name=request.POST["first_name"], last_name=request.POST["last_name"], password=request.POST["password"])
        user.save()
        return JsonResponse({ "success": True })
    elif request.method == 'DELETE':
        user=User.objects.get(id=user_id);
        user.delete()
    #elif request.method == 'PUT':

@csrf_exempt
def transactions(request, transaction_id=-1):
    if request.method == 'GET':
        if transaction_id == -1:
            return JsonResponse(serializers.serialize('json', Transaction.objects.all()), safe=False)
        else:
            try:
                transaction = Transaction.objects.get(pk=transaction_id)
                return JsonResponse(serializers.serialize('json', transaction), safe=False)
            except Transaction.DoesNotExist:
                return JsonResponse({ 'success': False})
    elif request.method == 'POST':
        transaction = Transaction(payer_id=request.POST["payer_id"], receiver_id=request.POST["receiver_id"], blog_post_id=request.POST["blog_post_id"], amount=request.POST["amount"])
        transaction.save()
        return JsonResponse({ "success": True })
    elif request.method == 'DELETE':
        transaction=Transaction.objects.get(id=transaction_id);
        transaction.delete()
    #elif request.method == 'PUT':

@csrf_exempt
def posts(request, post_id=-1):
    if request.method == 'GET':
        if post_id == -1:
            return JsonResponse(serializers.serialize('json', BlogPost.objects.all()), safe=False)
        else:
            try:
                post_post = BlogPost.objects.get(pk=post_id)
                return JsonResponse(serializers.serialize('json', blog_post), safe=False)
            except BlogPost.DoesNotExist:
                return JsonResponse({ 'success': False})
    elif request.method == 'POST':
        post = BlogPost(title=request.POST["title"], body=request.POST["body"], author_id=request.POST["author_id"])
        post.save()
        return JsonResponse({ "success": True })
    elif request.method == 'DELETE':
        post=Post.objects.get(id=post_id);
        post.delete()
    #elif request.method == 'PUT':

@csrf_exempt
def comments(request, comment_id=-1):
    if request.method == 'GET':
        if comment_id == -1:
            return JsonResponse(serializers.serialize('json', Comment.objects.all()), safe=False)
        else:
            try:
                comment = Comment.objects.get(pk=comment_id)
                return JsonResponse(serializers.serialize('json', comment), safe=False)
            except Comment.DoesNotExist:
                return JsonResponse({ 'success': False})
    elif request.method == 'POST':
        comment = Comment(blog_post_id=request.POST["blog_post_id"], author_id=request.POST["author_id"], text=request.POST["text"])
        comment.save()
        return JsonResponse({ "success": True })
    elif request.method == 'DELETE':
        comment=Comment.objects.get(id=comment_id);
        comment.delete();
    #elif request.method == 'PUT':

def test(request):
    return JsonResponse({ "success": True })
