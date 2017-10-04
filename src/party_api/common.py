from typing import Type

from django.http.response import HttpResponseNotAllowed
from api_commons.common import BaseController, ApiResponse, exception_handler
from rest_framework.permissions import IsAuthenticated, AllowAny


class PCalcGeneralPermission(IsAuthenticated):
    pass


class PCalcAuthPermission(AllowAny):
    pass


class BasePCalcAuthController(BaseController):
    permission_classes = (PCalcAuthPermission,)

    def get(self, *args, **kwargs):
        return HttpResponseNotAllowed([])

    def post(self, *args, **kwargs):
        return HttpResponseNotAllowed([])


class BasePCalcController(BaseController):
    permission_classes = (PCalcGeneralPermission,)

    def get(self, *args, **kwargs):
        return HttpResponseNotAllowed([])

    def post(self, *args, **kwargs):
        return HttpResponseNotAllowed([])


def inject_dto(dto_type: Type):
    def inject_dto_wrap(func):
        def wrapper(*args, **kwargs):
            request = args[1]
            dto = dto_type(request.data)
            if not dto.is_valid():
                return ApiResponse.bad_request(dto)
            args = args + (dto,)
            return func(*args, **kwargs)

        return wrapper

    return inject_dto_wrap


def party_api_exception_handler(ex, context):
    return exception_handler(ex, context)
