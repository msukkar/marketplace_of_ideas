from django.http import HttpResponse, JsonResponse
from django.core import serializers
from django import db
from model_api.models import *
from django.views.decorators.csrf import csrf_exempt
import os
import hmac
from model_api import settings
from django.contrib.auth import hashers

@csrf_exempt
def users(request, user_id=-1):
    if request.method == 'GET':
        if user_id == -1:
            return JsonResponse({
                                    'success': True,                                                \
                                    'response': serializers.serialize('json', User.objects.all())   \
                                }, safe=False)
        else:
            try:
                user = User.objects.get(pk=user_id)
                return JsonResponse({
                                        'success': True,                                        \
                                        'response': serializers.serialize('json', [user])       \
                                    }, safe=False)
            except User.DoesNotExist:
                return JsonResponse({
                                        'success': False,                           \
                                        'response': 'No user with that id exists'   \
                                    })

    elif request.method == 'POST':
        if not user_id == -1:
            try:
                if 'username' not in request.POST or        \
                   'first_name' not in request.POST or      \
                   'last_name' not in request.POST or       \
                   'password' not in request.POST:
                    return JsonResponse({
                                            'success': False,                           \
                                            'response': 'Missing required field(s)'     \
                                        })

                user = User.objects.filter(pk=user_id)                               \
                                   .update(username=request.POST['username'],        \
                                           first_name=request.POST['first_name'],    \
                                           last_name=request.POST['last_name'],      \
                                           password=request.POST['password']         \
                                          )
                return JsonResponse({
                                        'success': True,                            \
                                        'id': user_id,                              \
                                        'username': request.POST['username'],       \
                                        'first_name': request.POST['first_name'],   \
                                        'last_name': request.POST['last_name']      \
                                    })
            except User.DoesNotExist:
                return JsonResponse({
                                        'success': False,                           \
                                        'response': 'No user with that id exists'   \
                                    })
        return JsonResponse({
                                'success': False,               \
                                'response': 'No id specified'   \
                            })

    elif request.method == 'DELETE':
        try:
            user = User.objects.get(pk=user_id)
            user.delete()
            return JsonResponse({ 'success': True, 'user': user_id })
        except User.DoesNotExist:
            return JsonResponse({ 'success': False, 'response': 'No user with that id exists' })

@csrf_exempt
def sign_in(request):
    if 'username' not in request.POST or \
       'password' not in request.POST:
        return JsonResponse({
                                'success': False,                       \
                                'response': 'Missing required field(s)' \
                            })

    user = User.objects.get(username=request.POST['username'])
    if hashers.check_password(request.POST['password'], user.password):
        authenticator = hmac.new(key = settings.SECRET_KEY.encode('utf-8'), msg = os.urandom(32)).hexdigest()
        authenticator = Authenticator(
            user_id=user.id,
            authenticator=authenticator
            )
        try:
            authenticator.save()
        except db.Error:
            return JsonResponse({ 'success': False, 'response': 'db error' })
        return JsonResponse({
                                'success': True,                       \
                                'authenticator': authenticator.authenticator \
                            })
    else:
        return JsonResponse({
                                'success': False,                       \
                                'response': 'Invalid username and password combination' \
                            })

@csrf_exempt
def sign_out(request):
    if 'authenticator' not in request.POST:
        return JsonResponse({
                                'success': False,                       \
                                'response': 'Missing required field(s)' \
                            })

    try:
        authenticator = Authenticator.objects.get(authenticator = request.POST['authenticator'])
        authenticator.delete()
        return JsonResponse({
                                'success': True,                       \
                                'response': 'Successfully signed out' \
                            })
    except Authenticator.DoesNotExist:
        return JsonResponse({
                                'success': False,                                   \
                                'response': 'No authenticator with that authenticator exists'    \
                            })

@csrf_exempt
def create_user(request):
    if 'username' not in request.POST or    \
       'first_name' not in request.POST or  \
       'last_name' not in request.POST or   \
       'password' not in request.POST:
        return JsonResponse({
                                'success': False,                       \
                                'response': 'Missing required field(s)' \
                            })

    password = hashers.make_password(request.POST['password'])
    #return HttpResponse(password)
    user = User(username=request.POST['username'],              \
                first_name=request.POST['first_name'],          \
                last_name=request.POST['last_name'],            \
                password=password                               \
                )

    try:
        user.save()
    except db.Error:
        return JsonResponse({ 'success': False, 'response': 'db error' })

    return JsonResponse({ 
                            'success': True,                            \
                            'username': request.POST['username'],       \
                            'first_name': request.POST['first_name'],   \
                            'last_name': request.POST['last_name']      \
                        })

@csrf_exempt
def transactions(request, transaction_id=-1):
    if request.method == 'GET':
        if transaction_id == -1:
            return JsonResponse({
                                    'success': True,                                                        \
                                    'response': serializers.serialize('json', Transaction.objects.all())    \
                                }, safe=False)
        else:
            try:
                transaction = Transaction.objects.get(pk=transaction_id)
                return JsonResponse({
                                        'success': True,                                            \
                                        'response': serializers.serialize('json', [transaction])    \
                                    }, safe=False)
            except Transaction.DoesNotExist:
                return JsonResponse({
                                        'success': False,                                   \
                                        'response': 'No transaction with that id exists'    \
                                    })
    elif request.method == 'POST':
        if not transaction_id == -1:
            try:
                if 'payer_id' not in request.POST or        \
                   'receiver_id' not in request.POST or     \
                   'blog_post_id' not in request.POST or    \
                   'amount' not in request.POST:
                    return JsonResponse({
                                            'success': False,                       \
                                            'response': 'Missing required field(s)' \
                                        })
                transaction = Transaction.objects.filter(pk=transaction_id)                           \
                                                 .update(payer_id=request.POST['payer_id'],           \
                                                         receiver_id=request.POST['receiver_id'],     \
                                                         blog_post_id=request.POST['blog_post_id'],   \
                                                         amount=request.POST['amount']                \
                                                        )
                return JsonResponse({
                                        'success': True,                            \
                                        'id': transaction_id,                       \
                                        'payer_id': request.POST['payer_id'],       \
                                        'receiver_id': request.POST['receiver_id'], \
                                        'amount': request.POST['amount']            \
                                    })
            except Transaction.DoesNotExist:
                return JsonResponse({
                                        'success': False,                                   \
                                        'response': 'No transaction with that id exists'    \
                                    })
        return JsonResponse({ 'success': False, 'response': 'No id specified' })
    elif request.method == 'DELETE':
        try:
            transaction = Transaction.objects.get(pk=transaction_id)
            transaction.delete()
            return JsonResponse({ 'success': True, 'id': transaction_id })
        except Transaction.DoesNotExist:
            return JsonResponse({ 'success': False, 'response': 'No transaction with that id exists' })

@csrf_exempt
def create_transaction(request):
    if 'payer_id' not in request.POST or        \
       'receiver_id' not in request.POST or     \
       'blog_post_id' not in request.POST or    \
       'amount' not in request.POST:
        return JsonResponse({ 'success': False, 'response': 'Missing required field(s)' })

    transaction = Transaction(payer_id=request.POST['payer_id'],            \
                              receiver_id=request.POST['receiver_id'],      \
                              blog_post_id=request.POST['blog_post_id'],    \
                              amount=request.POST['amount']                 \
                             )

    try:
        transaction.save()
    except db.Error:
        return JsonResponse({ 'success': False, 'response': 'db error' })

    return JsonResponse({
                          'success': True,                                  \
                          'payer_id': request.POST['payer_id'],             \
                          'receiver_id': request.POST['receiver_id'],       \
                          'amount': request.POST['amount']                  \
                        })

@csrf_exempt
def posts(request, post_id=-1):
    if request.method == 'GET':
        if post_id == -1:
            return JsonResponse({ 
                                    'success': True,                                                    \
                                    'response': serializers.serialize('json', BlogPost.objects.all())   \
                                }, safe=False)
        else:
            try:
                blog_post = BlogPost.objects.get(pk=post_id)
                return JsonResponse({
                                        'success': True,                                        \
                                        'response': serializers.serialize('json', [blog_post])  \
                                    }, safe=False)
            except BlogPost.DoesNotExist:
                return JsonResponse({ 'success': False, 'response': 'No blog post with that id exists' })
    elif request.method == 'POST':
        if not post_id == -1:
            try:
                if 'title' not in request.POST or       \
                    'authenticator' not in request.POST or \
                   'body' not in request.POST:
                    return JsonResponse({ 'success': False, 'response': 'Missing required field(s)' })
                authenticator = Authenticator.objects.get(authenticator=request.POST['authenticator'])
                post = BlogPost.objects.filter(pk=post_id)                          \
                                       .update(title=request.POST['title'],         \
                                               body=request.POST['body'],           \
                                               author_id=authenticator.user_id
                                              )
                return JsonResponse({
                                        'success': True,                        \
                                        'id': post_id,                          \
                                        'title': request.POST['title'],         \
                                        'body': request.POST['body'],           \
                                        'author': authenticator.user_id     \
                                    })
            except BlogPost.DoesNotExist:
                return JsonResponse({ 'success': False, 'response': 'No blog post with that id exists' })
            except Authenticator.DoesNotExist:
                return JsonResponse({ 'success': False, 'response': 'No authentication' })
        return JsonResponse({ 'success': False, 'response': 'No id specified' })
    elif request.method == 'DELETE':
        try:
            blog_post = BlogPost.objects.get(pk=post_id)
            blog_post.delete()
            return JsonResponse({ 'success': True, 'id': post_id })
        except BlogPost.DoesNotExist:
            return JsonResponse({ 'success': False, 'response': 'No blog post with that id exists' })

@csrf_exempt
def create_post(request):
    if 'title' not in request.POST or       \
       'authenticator' not in request.POST or \
       'body' not in request.POST:
        return JsonResponse({ 'success': False, 'response': 'Missing required field(s)' })

    try:
        authenticator = Authenticator.objects.get(authenticator=request.POST['authenticator'])
    except Authenticator.DoesNotExist:
        return JsonResponse({ 'success': False, 'response': 'No authentication' })

    post = BlogPost(title=request.POST['title'],            \
                    body=request.POST['body'],              \
                    author_id=authenticator.user_id
                   )
    try:
        post.save()
    except db.Error:
        return JsonResponse({ 'success': False, 'response': 'db error' })

    return JsonResponse({ 
                          'success': True,                      \
                          'title': request.POST['title'],       \
                          'body': request.POST['body'],         \
                          'author': authenticator.user_id
                        })


@csrf_exempt
def comments(request, comment_id=-1):
    if request.method == 'GET':
        post_id = request.GET.get('post_id', '-1')

        if comment_id == -1:
            if post_id != '-1':
                comments = Comment.objects.all().filter(blog_post=post_id)
                return JsonResponse(serializers.serialize('json', comments), safe=False)
            return JsonResponse(serializers.serialize('json', Comment.objects.all()), safe=False)
        else:
            try:
                comment = Comment.objects.get(pk=comment_id)
                return JsonResponse(serializers.serialize('json', [comment]), safe=False)
            except Comment.DoesNotExist:
                return JsonResponse({ 'success': False, 'response': 'No comment with that id exists' })
    elif request.method == 'POST':
        if not comment_id == -1:
            try:
                if 'blog_post_id' not in request.POST or 'author_id' not in request.POST or 'text' not in request.POST:
                    return JsonResponse({ 'success': False, 'response': 'Missing required field(s)' })
                comment = Comment.objects.filter(pk=comment_id).update(blog_post_id=request.POST['blog_post_id'], author_id=request.POST['author_id'], text=request.POST['text'])
                return JsonResponse({ 'success': True, 'id': comment_id, 'blog_post_id': request.POST['blog_post_id'], 'author_id': request.POST['author_id'], 'text': request.POST['text'] })
            except Comment.DoesNotExist:
                return JsonResponse({ 'success': False, 'response': 'No comment with that id exists' })
        return JsonResponse({ 'success': False, 'response': 'No id specified' })
    elif request.method == 'DELETE':
        try:
            comment = Comment.objects.get(pk=comment_id)
            comment.delete();
            return JsonResponse({ 'success': True })
        except Comment.DoesNotExist:
            return JsonResponse({ 'success': False, 'response': 'No comment with that id exists' })

@csrf_exempt
def create_comment(request):
    if 'blog_post_id' not in request.POST or    \
       'author_id' not in request.POST or       \
       'text' not in request.POST:
        return JsonResponse({ 'success': False, 'response': 'Missing required field(s)' })

    comment = Comment(blog_post_id=request.POST['blog_post_id'],    \
                      author_id=request.POST['author_id'],          \
                      text=request.POST['text']                     \
                     )

    try:
        comment.save()
    except db.Error:
        return JsonResponse({ 'success': False, 'response': 'db error' })

    return JsonResponse({
                            'success': True,                                \
                            'blog_post_id': request.POST['blog_post_id'],   \
                            'author_id': request.POST['author_id'],         \
                            'text': request.POST['text']                    \
                        })

def test(request):
    return JsonResponse({ 'success': True })
