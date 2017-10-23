from api_commons.common import ApiResponse
from django.http import HttpRequest
from party_api.common import BasePCalcController, inject_dto
from party_api.controllers.party.dtos import PartyDto
from party_api.models import Party
from party_api.services.party_service import update_party_by_id, delete_party_by_id, create_party


class PartyListController(BasePCalcController):
    def get(self, request: HttpRequest):
        parties = Party.objects.all()
        return ApiResponse.success(PartyDto.from_model_list(parties))


class PartyController(BasePCalcController):
    def get(self, request: HttpRequest, id):
        party = Party.objects.get(pk=id)
        if party is not None:
            return ApiResponse.success(PartyDto.from_model(party))
        return ApiResponse.not_found("Party does not exist")

    @inject_dto(PartyDto)
    def put(self, request: HttpRequest, party_dto: PartyDto, id):
        party = update_party_by_id(id, party_dto)
        return ApiResponse.success(party)

    def delete(self, request: HttpRequest, id):
        return ApiResponse.success(delete_party_by_id(id))

    @inject_dto(PartyDto)
    def post(self, request: HttpRequest, party_dto: PartyDto, id):
        party = create_party(party_dto)
        return ApiResponse.success(party)
