from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework.test import force_authenticate
from django.contrib.auth.models import User, Group

class UserTests(APITestCase):
    def test_create_user(self):
        """
        Ensure we can create a new user object.
        """
        User.objects.create_user(username='admin', email="m@m.com")
        user = User.objects.get(username='admin')
        data = {'username': 'foobar', 'email': 'm@m.com'}
        self.client.force_authenticate(user=user)
        response = self.client.post('/users/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User.objects.count(), 2)
        self.assertEqual(User.objects.get(username='foobar'), 'foobar')
    