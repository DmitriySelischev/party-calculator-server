from party_api.controllers.party.dtos import PartyDto
from party_api.models import Party


def update_party_by_id(id, party_dto: PartyDto):
    single_party = Party.objects.get(pk=id)
    single_party.name = party_dto.validated_data.get("name")
    single_party.description = party_dto.validated_data.get("description")
    single_party.save()
    return PartyDto.from_model(single_party)


def delete_party_by_id(id):
    party = Party.objects.get(pk=id)
    party.delete()
    return PartyDto.from_model(party)


def create_party(party_dto):
    party = Party.objects.create(name=party_dto.validated_data.get("name"),
                                 description=party_dto.validated_data.get("description"))
    party.save()
    return PartyDto.from_model(party)
