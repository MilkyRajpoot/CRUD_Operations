from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import postApi
from rest_framework import status
from .serializers import PostSerializer
from django.http import HttpResponse,JsonResponse
from django.http import *
from django.shortcuts import get_object_or_404 

# Create your views here.

def index(request):
    return HttpResponse("Hello, world. You're at the employeeList index.")

class InfoView(APIView):
    def get(self, request):
        query = postApi.objects.all()
        serializercls = PostSerializer(query, many=True)
        return Response(serializercls.data)
