from api_commons.common import ApiResponse
from django.contrib.auth import authenticate, login, logout
from django.http import HttpRequest

from party_api.common import BasePCalcAuthController, BasePCalcController, inject_dto
from party_api.controllers.security.dtos import LoginInDto, LoginOutDto


class LoginController(BasePCalcAuthController):
    @inject_dto(LoginInDto)
    def post(self, request: HttpRequest, dto: LoginInDto):
        user = authenticate(request, username=dto.validated_data.get('username'), password=dto.validated_data.get('password'))
        if user:
            login(request, user)
            return ApiResponse.success(LoginOutDto.from_user(user))
        return ApiResponse.not_authenticated()


class LogoutController(BasePCalcController):
    def get(self, request):
        logout(request)
        return ApiResponse.success()
