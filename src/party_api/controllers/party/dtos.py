from api_commons.dto import BaseDto, empty
from party_api.models import Party
from rest_framework import serializers


class PartyDto(BaseDto):
    id = serializers.IntegerField(required=False)
    name = serializers.CharField()
    description = serializers.CharField()

    @classmethod
    def from_model(cls, party: Party):
        dto = cls()
        dto.id = party.pk
        dto.name = party.name
        dto.description = party.description
        return dto

    @classmethod
    def from_model_list(cls, parties: []):
        party_list = []
        for party in parties:
            dto = cls.from_model(party)
            party_list.append(dto)
        return party_list
