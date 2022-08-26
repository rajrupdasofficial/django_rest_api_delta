from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from .models import Snippet
from .serializers import SnippetSerializer
# Create your views here.


""" root api to list all types of snippets or can create a new snippets"""
@csrf_exempt
def snippet_list(request):
    """List all snippets"""
    if request.method == "GET":
        snippets = Snippet.objects.all()
        serializer = SnippetSerializer(snippets,many=True)
        return JsonResponse(serializer.data,safe=False)
    elif request.method == "POST":
        data =JSONParser().parse(request)
        serializer = SnippetSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data,status=201)
        return JsonResponse(serializer.errors,status=400)
"""As we wont have a csrf token we have to mark the csrf_exempt to able to perfrm some client side POST"""

@csrf_exempt
def snippet_detail(request,pk):
    """ Receive , update or delete a code snippet """
    try:
        snippet= Snippet.objects.get(pk=pk)
    except Snippet.DoesNotExist:
        return HttpResponse(status=404)
    if request.method == "GET":
        serializer = SnippetSerializer(snippet)
        return JsonResponse(serializer.data)
    elif request.method == "PUT":
        data = JSONParser().parse(request)
        serializer = SnippetSerializer(snippet,data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors,status=400)
    elif request.method == 'DELETE':
        snippet.delete()
        return HttpResponse(status=404)

