from __future__ import annotations

from typing import Any, ClassVar

from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    class Meta:
        constraints: ClassVar = [
            models.UniqueConstraint(fields=["username"], name="unique_username"),
            models.UniqueConstraint(fields=["email"], name="unique_email"),
        ]

    @classmethod
    def create_user(
        cls,
        username: str,
        email: str | None = None,
        password: str | None = None,
        **extra_fields: Any,
    ) -> User:
        if not username:
            msg = "The given username must be set"
            raise ValueError(msg)
        if not password:
            msg = "The given password must be set"
            raise ValueError(msg)
        email = cls.normalize_email(email) if email else ""
        user = cls(username=username, email=email, **extra_fields)
        user.set_password(password)
        user.full_clean()
        user.save(using=cls._db)
        return user

    @classmethod
    def create_superuser(
        cls,
        username: str,
        email: str | None = None,
        password: str | None = None,
        **extra_fields: Any,
    ) -> User:
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            msg = "Superuser must have is_staff=True."
            raise ValueError(msg)
        if extra_fields.get("is_superuser") is not True:
            msg = "Superuser must have is_superuser=True."
            raise ValueError(msg)

        return cls.create_user(username, email, password, **extra_fields)
