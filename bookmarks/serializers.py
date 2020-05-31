from rest_framework import serializers
from bookmarks.models import Bookmark


class BookmarkSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    created_at = serializers.DateTimeField(required=True)
    updated_at = serializers.DateTimeField(required=False)
    title = serializers.CharField(required=False, allow_blank=True, max_length=200)
    url = serializers.URLField(required=True)
    is_public = serializers.BooleanField(required=False)


    def create(self, validated_data):
        """
        Create and return a new `Bookmark` instance, given the validated data.
        """
        return Bookmark.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Bookmark` instance, given the validated data.
        """
        instance.title = validated_data.get('title', instance.title)
        instance.url = validated_data.get('url', instance.url)
        instance.is_public = validated_data.get('is_public', instance.is_public)
        instance.save()
        return instance