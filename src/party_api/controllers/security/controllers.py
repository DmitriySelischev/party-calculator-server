from api_commons.common import ApiResponse
from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpRequest
from django.contrib.auth.models import User
from party_api.common import BasePCalcAuthController, BasePCalcController, inject_dto
from party_api.controllers.security.dtos import LoginInDto, LoginOutDto, SignUpDto


class LoginController(BasePCalcAuthController):
    @inject_dto(LoginInDto)
    def post(self, request: HttpRequest, dto: LoginInDto):
        user = authenticate(request, username=dto.validated_data.get('username'),
                            password=dto.validated_data.get('password'))
        if user:
            login(request, user)
            return ApiResponse.success(LoginOutDto.from_user(user))
        return ApiResponse.not_authenticated()


class LogoutController(BasePCalcController):
    def get(self, request):
        logout(request)
        return ApiResponse.success()


class RestoreSessionController(BasePCalcController):
    def get(self, request):
        return ApiResponse.success(LoginOutDto.from_user(request.user))


class SignUpController(BasePCalcAuthController):
    @inject_dto(SignUpDto)
    def post(self, request: HttpRequest, dto: SignUpDto):
        if not dto.is_valid():
            return ApiResponse.bad_request()
        try:
            new_user = User.objects.create_user(username=dto.validated_data.get('username'),
                                                email=dto.validated_data.get('email'),
                                                password=dto.validated_data.get('password'),
                                                first_name=dto.validated_data.get('first_name'),
                                                last_name=dto.validated_data.get('last_name'))
            new_user.save()
        except IntegrityError as e:
            return ApiResponse.not_authenticated()
        user = authenticate(request,
                            username=dto.validated_data.get('username'), password=dto.validated_data.get('password'))
        if user:
            login(request, user)
            return ApiResponse.success(LoginOutDto.from_user(user))
        return ApiResponse.not_authenticated()
