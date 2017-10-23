from api_commons.common import ApiResponse
from django.http import HttpRequest
from party_api.common import BasePCalcController, inject_dto
from party_api.controllers.party.dtos import PartyDto
from party_api.models import Party


class PartyListController(BasePCalcController):

    def get(self, request: HttpRequest):
        parties = Party.objects.all()
        return ApiResponse.success(PartyDto.from_model_list(parties))
