from django.conf.urls import url
from party_api.controllers.security import controllers

urlpatterns = [
    url(r'^user/list', controllers.LoginController.as_view(), name='user_list'),
    url(r'^signup$', controllers.SignUpController.as_view(), name='signup'),
    url(r'^logout$', controllers.LogoutController.as_view(), name='logout'),
    url(r'^restore-session', controllers.RestoreSessionController.as_view(), name='restore-session'),
]
