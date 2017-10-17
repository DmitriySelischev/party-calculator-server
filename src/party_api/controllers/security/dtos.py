from api_commons.dto import BaseDto, empty
from django.contrib.auth.models import User
from rest_framework import serializers


class LoginInDto(BaseDto):
    username = serializers.CharField()
    password = serializers.CharField()


class LoginOutDto(BaseDto):
    id = serializers.IntegerField()
    username = serializers.CharField()
    email = serializers.EmailField()

    @classmethod
    def from_user(cls, user: User):
        dto = cls()
        dto.id = user.pk
        dto.username = user.username
        dto.email = user.email
        return dto


class SignUpDto(BaseDto):
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    username = serializers.CharField()
    email = serializers.EmailField()
    password = serializers.CharField()
