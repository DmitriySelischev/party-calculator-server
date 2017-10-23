from api_commons.dto import BaseDto, empty
from party_api.models import Party
from rest_framework import serializers


class PartyDto(BaseDto):
    name = serializers.CharField()
    description = serializers.CharField()

    @classmethod
    def from_model(cls, party: Party):
        dto = cls()
        dto.id = party.pk
        dto.name = party.name
        dto.description = party.description
        return dto
