from party_api.common import BaseModelOperationsService
from party_api.models import Party


class PartyService(BaseModelOperationsService):
    model = Party
