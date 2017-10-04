from django.conf.urls import url
from party_api.controllers.security import controllers

urlpatterns = [
    url(r'^login$', controllers.LoginController.as_view(), name='login'),
    url(r'^logout$', controllers.LogoutController.as_view(), name='logout'),
]
