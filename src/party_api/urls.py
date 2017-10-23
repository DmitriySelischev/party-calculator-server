from django.conf.urls import url, include

urlpatterns = [
    url(r'^security/?', include('party_api.controllers.security.urls', namespace='security')),
    url(r'^party/?', include('party_api.controllers.party.urls', namespace='party')),
]
