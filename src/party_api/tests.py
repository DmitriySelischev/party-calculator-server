from django.test import TestCase, Client
from django.contrib.auth.models import User

SECURITY_API = '/api/security'


class BaseTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='artem', email='artem@mail.com', password='123456')


# Create your tests here.
class LoginTestCase(BaseTestCase):
    def test_user_can_login(self):
        response = self.client.post('%s/login' % SECURITY_API, {'username': 'artem', 'password': '123456'})
        assert response.status_code == 200
        assert response.data.payload.email == 'artem@mail.com'
        assert response.data.payload.username == 'artem'

    def test_user_unauthorized(self):
        response = self.client.post('%s/login' % SECURITY_API, {'username': 'user2', 'password': 'password'})
        assert response.status_code == 401


class RefreshSessionTestCase(BaseTestCase):
    def test_user_can_refresh_session(self):
        self.client.post('%s/login' % SECURITY_API, {'username': 'artem', 'password': '123456'})
        response = self.client.get('%s/restore-session' % SECURITY_API)
        assert response.status_code == 200

    def test_unauthorized_user_can_not_refresh_session(self):
        response = self.client.get('%s/restore-session' % SECURITY_API)
        assert response.status_code == 401


class LogoutTestCase(BaseTestCase):
    def test_user_can_logout(self):
        self.client.post('%s/login' % SECURITY_API, {'username': 'artem', 'password': '123456'})
        response = self.client.get('%s/logout' % SECURITY_API)
        assert response.status_code == 200

    def _test_unauthorized_user_can_not_logout(self):
        response = self.client.get('%s/logout' % SECURITY_API)
        assert response.status_code == 401


class SignUpTestCase(BaseTestCase):
    def test_unauthorized_user_can_signup(self):
        response = self.client.post('%s/signup' % SECURITY_API,
                                    {'username': 'user1', 'password': '123456', 'email': 'user1@email.com',
                                     'first_name': 'user', 'last_name': 'userr'})
        assert response.status_code == 200

    def test_authorized_user_can_not_signup(self):
        self.client.post('%s/login' % SECURITY_API, {'username': 'artem', 'password': '123456'})
        response = self.client.post('%s/signup' % SECURITY_API,
                                    {'username': 'user1', 'password': '123456', 'email': 'user1@email.com',
                                     'first_name': 'user', 'last_name': 'userr'})
        assert response.status_code == 400
