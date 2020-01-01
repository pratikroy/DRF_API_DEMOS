import json

from django.contrib.auth.models import User
from django.urls import reverse

from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase

from profiles.models import Profile
from profiles.serializers import ProfileSerializer


class RegistrationTestCase(APITestCase):

    def test_registration(self):
        data = {
            "username": "testUser",
            "email": "test@testmail.com",
            "password1": "testPassword",
            "password2": "testPassword"
        }

        response = self.client.post("/api/rest-auth/registration/", data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
