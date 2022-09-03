from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Snippet
from .serializers import SnippetSerializer
from rest_framework import generics
from rest_framework import mixins
# Create your views here.


""" root api to list all types of snippets or can create a new snippets"""
"""@csrf_exempt
def snippet_list(request):
    List all snippets
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
As we wont have a csrf token we have to mark the csrf_exempt to able to perfrm some client side POST

@csrf_exempt
def snippet_detail(request,pk):
     Receive , update or delete a code snippet
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
        return HttpResponse(status=404)"""
class SnippetList(mixins.ListModelMixin,mixins.CreateModelMixin,generics.GenericAPIView):
    queryset=Snippet.objects.all()
    serializer_class = SnippetSerializer
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
    """def get(self,reuest,format=None):
        snippets = Snippet.objects.all()
        serializer = SnippetSerializer(snippets,many=True)
        return Response(serializer.data)
    def post(self,request,format=None):
        serializer = SnippetSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)"""
class SnippetDetail(mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin,
                    generics.GenericAPIView):
     queryset = Snippet.objects.all()
     serializer_class = SnippetSerializer
     def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
     def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
     def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
     """CRUD operation
     def get_object(self,pk):
        try:
            return Snippet.objects.get(pk=pk)
        except Snippet.DoesNotExist:
            raise Http404
     def get(self,request,pk,format=None):
        snippet = self.get_object(pk)
        serializer =  SnippetSerializer(snippet,data=request.data)
        if serializer.is_valid():
            serializer.save
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
     def put(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = SnippetSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
     def delete(self,request,pk,format=None):
        snippet = slef.get_object(pk)
        snippet.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)"""


