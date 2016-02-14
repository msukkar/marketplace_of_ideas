from django.http import JsonResponse
from django.core import serializers
from marketplace_of_ideas.models import *

def test(request):
    return JsonResponse(serializers.serialize('json', User.objects.all()), safe=False)