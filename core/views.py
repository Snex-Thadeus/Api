from django.shortcuts import render
from django.http import JsonResponse

from rest_framework.response import Response
from rest_framework.views import APIView

from rest_framework.permissions import IsAuthenticated
from .serializers import PostSerializer
from .models import Post
from rest_framework import generics, mixins


class PostView(mixins.ListModelMixin, mixins.CreateModelMixin,
               generics.GenericAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.all()

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class PostCreateView(mixins.ListModelMixin, generics.CreateAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.all()

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class PostListCreateView(generics.ListCreateAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.all()


class TestView(APIView):

    permission_classes = (IsAuthenticated,)

    def get(self, request, *args, **kwargs):
        qs = Post.objects.all()
        serializer = PostSerializer(qs, many=True)
        return Response(serializer.data)

    def post(self, requset, *args, **kwargs):
        serializer = PostSerializer(data=requset.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

