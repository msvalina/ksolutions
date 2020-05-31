from bookmarks.models import Bookmark
from django.contrib.auth.models import User
from bookmarks.serializers import BookmarkSerializer, UserSerializer
from rest_framework import generics
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework import permissions
from rest_framework.response import Response


class BookmarkList(generics.ListCreateAPIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Bookmark.objects.all()
    serializer_class = BookmarkSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
    
    def list(self, request):
        if not request.user.is_authenticated:
            queryset1 = Bookmark.objects.all().filter(is_public=True)
            serializer1 = BookmarkSerializer(queryset1, many=True)
            return Response(serializer1.data)

        queryset1 = Bookmark.objects.all().filter(is_public=True)
        queryset2 = Bookmark.objects.all().filter(owner=request.user.id)
        serializer1 = BookmarkSerializer(queryset1, many=True)
        serializer2 = BookmarkSerializer(queryset2, many=True)
        data = serializer1.data + serializer2.data
        return Response(data)



class BookmarkDetail(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    queryset = Bookmark.objects.all()
    serializer_class = BookmarkSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
