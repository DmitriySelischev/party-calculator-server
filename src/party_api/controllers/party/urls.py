from django.conf.urls import url
from party_api.controllers.party import controllers

urlpatterns = [
    url(r'^list', controllers.PartyListController.as_view(), name='party_list'),
    url(r'^(?P<id>\d+)?$', controllers.PartyController.as_view(), name='party_single'),
]
