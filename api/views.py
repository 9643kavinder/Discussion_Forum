from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import CustomUser, Speciality, Post
from .serializers import PostSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


def home(request):
    return HttpResponse("<h1>Hello World</h1>")


class PostView(APIView):
    """
    List all post of speciality
    """
    def get(self, request, name, format=None):
        post_snippets = Speciality.objects.get(name=name).post_set.all()
        serializer = PostSerializer(post_snippets, many=True)
        return Response(serializer.data)


