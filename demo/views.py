from django.shortcuts import render
from django.http import HttpResponse
from django.views import View


from rest_framework import viewsets
from .serializers import BookSerializer
from .models import Book

class BookViewSet(viewsets.ModelViewSet):
  serializer_class = BookSerializer
  queryset = Book.objects.all()

# Create your views here.

def home(request):
    return HttpResponse('some text')

def first(request):

 return HttpResponse('First message from Views')

class Another(View):

 def get(self,request):

   return HttpResponse('This is another function inside class')