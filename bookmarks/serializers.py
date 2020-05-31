from django.contrib.auth.models import User
from rest_framework import serializers
from bookmarks.models import Bookmark


class BookmarkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bookmark
        fields = ['id', 'title', 'url', 'is_public', 'owner', 'created_at', 'updated_at']

class UserSerializer(serializers.ModelSerializer):
    bookmarks = serializers.PrimaryKeyRelatedField(many=True, queryset=Bookmark.objects.all())

    class Meta:
        model = User
        fields = ['id', 'username', 'email',  'bookmarks']