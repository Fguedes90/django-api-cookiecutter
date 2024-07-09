from __future__ import annotations

import pytest
from django.db.utils import IntegrityError
from django.test import TestCase

from api.user.models import User


class UserModelTest(TestCase):

    def setUp(self) -> None:
        self.user_data = {
            "username": "testuser",
            "password": "testpass",
            "email": "testuser@example.com",
        }
        self.superuser_data = {
            "username": "admin",
            "password": "adminpass",
            "email": "admin@example.com",
        }

    def test_create_user(self) -> None:
        user = User.objects.create_user(**self.user_data)
        assert user.username == self.user_data["username"]
        assert user.check_password(self.user_data["password"])
        assert user.email == self.user_data["email"]
        assert not user.is_staff
        assert not user.is_superuser

    def test_create_user_without_username(self) -> None:
        self.user_data.pop("username")
        with pytest.raises(TypeError):
            User.objects.create_user(**self.user_data)

    def test_create_user_without_email(self) -> None:
        self.user_data.pop("email")
        user = User.objects.create_user(**self.user_data)
        assert user.email == ""

    def test_create_user_with_existing_username(self) -> None:
        User.objects.create_user(**self.user_data)
        with pytest.raises(IntegrityError):
            User.objects.create_user(**self.user_data)
