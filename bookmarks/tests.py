from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework.test import force_authenticate
from django.contrib.auth.models import User, Group
from bookmarks.models import Bookmark


class BookmarkTests(APITestCase):
    def test_create_bookmark(self):
        """
        Ensure we can create a new bookmark object.
        """
        User.objects.create_user(username="admin", email="m@m.com")
        user = User.objects.get(username="admin")
        self.client.force_authenticate(user=user)
        data = {
            "is_public": True,
            "owner": 1,
            "title": "Foolish",
            "url": "http://foolish.com",
            "owner": 1,
        }
        response = self.client.post("/bookmarks/", data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Bookmark.objects.count(), 1)

