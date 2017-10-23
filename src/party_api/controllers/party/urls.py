from django.conf.urls import url
from party_api.controllers.party import controllers

urlpatterns = [
    url(r'^list', controllers.PartyListController.as_view(), name='party_list'),
]
