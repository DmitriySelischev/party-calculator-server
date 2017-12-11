from typing import Type
from api_commons.dto import BaseDto as Dto
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


class BaseDto(Dto):
    def update(self, instance, validated_data):
        pass

    def create(self, validated_data):
        pass

    @classmethod
    def from_model(cls, model):
        dto = cls()
        for field in dto.get_declared_fields():
            setattr(dto, field, model.pk)
        return dto

    @classmethod
    def from_model_list(cls, model_list: []):
        result_list = []
        for model in model_list:
            dto = cls.from_model(model)
            result_list.append(dto)
        return result_list


class BaseServiceMetaclass(type):
    def __init__(cls, name, bases, dct):
        super(BaseServiceMetaclass, cls).__init__(name, bases, dct)
        if cls.__name__ == 'BaseModelOperationsService':
            return
        if getattr(cls, 'model', None) is None:
            raise NotImplementedError("Model is not specified.")


class BaseModelOperationsService(metaclass=BaseServiceMetaclass):
    """
    this class provides basic entity functionality such as:
    1. return all entities
    2. get by id
    3. update entity by id
    4. delete entity by id
    5. create new entity
    """
    model = None

    @classmethod
    def get_all(cls):
        """:rtype <list>"""
        return cls.model.objects.all()

    @classmethod
    def get_by_id(cls, _id: int):
        dir(cls)
        return cls.transform_operation_result(cls.model.objects.get(pk=_id))

    @classmethod
    def update_by_id(cls, validated_data, _id: int):
        instance = cls.model.objects.get(pk=_id)
        for key in validated_data:
            setattr(instance, key, validated_data.get(key))
        instance.save()
        return cls.transform_operation_result(instance)

    @classmethod
    def delete_by_id(cls, _id: int):
        instance = cls.model.objects.get(pk=_id)
        instance.delete()
        return cls.transform_operation_result(instance)

    @classmethod
    def create(cls, validated_data):
        instance = cls.model.objects.create(**validated_data)
        instance.save()
        return cls.transform_operation_result(instance)

    @staticmethod
    def transform_operation_result(instance):
        return instance


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
