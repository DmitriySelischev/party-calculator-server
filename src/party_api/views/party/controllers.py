from api_commons.common import ApiResponse
from django.http import HttpRequest
from party_api.common import BasePCalcController, inject_dto
from party_api.views.party.dtos import PartyDto
from party_api.services.party_service import PartyService


class PartyListController(BasePCalcController):
    def get(self, request: HttpRequest):
        parties = PartyService.get_all()
        return ApiResponse.success(PartyDto.from_model_list(parties))


class PartyController(BasePCalcController):
    def get(self, request: HttpRequest, id: int):
        party_dto = PartyDto.from_model(PartyService.get_by_id(id))
        if party_dto is not None:
            return ApiResponse.success(party_dto)
        return ApiResponse.not_found("Party does not exist")

    @inject_dto(PartyDto)
    def put(self, request: HttpRequest, party_dto: PartyDto, _id: int):
        party = PartyService.update_by_id(_id, party_dto.validated_data)
        return ApiResponse.success(PartyDto.from_model(party))

    def delete(self, request: HttpRequest, _id: int):
        return ApiResponse.success(
            PartyDto.from_model(PartyService.delete_by_id(_id)))

    @inject_dto(PartyDto)
    def post(self, request: HttpRequest, party_dto: PartyDto):
        party = PartyService.create(party_dto.validated_data)
        return ApiResponse.success(PartyDto.from_model(party))
