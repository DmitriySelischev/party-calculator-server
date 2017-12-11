from django.conf.urls import url, include

urlpatterns = [
    url(r'^security/?', include('party_api.views.security.urls',
                                namespace='security')),
    url(r'^party/?', include('party_api.views.party.urls', namespace='party')),
]
