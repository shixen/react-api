from django.shortcuts import render
from rest_framework import generics, permissions
from drf_api.permissions import IsOwnerOrReadOnly
from .models import followers
from .serializers import followeSerializers


class FollowerList(generics.ListCreateAPIView):
    serializer_class = followeSerializers
    queryset = Follower.objects.all()
    permission_classes = [permission.IsOwnerOrReadOnly]
    

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class FollowerDetail(generics.RetrieveDestroyAPIView):
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Follower.objects.all()
    serializer_class = FollowerSerializer