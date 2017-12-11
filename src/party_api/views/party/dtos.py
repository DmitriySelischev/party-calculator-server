from party_api.common import BaseDto
from rest_framework import serializers


class PartyDto(BaseDto):
    id = serializers.IntegerField(required=False)
    name = serializers.CharField()
    description = serializers.CharField()

