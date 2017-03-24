from unittest import TestCase

from contrast_security.user_api.util import Util


class UtilTest(TestCase):
    def create_auth_token_test(self):
        username = 'reallyLongUserNameThatWould'
        service_key = 'someServiceKey'
        token = Util.create_authorization_token(username, service_key)
        self.assertEqual('cmVhbGx5TG9uZ1VzZXJOYW1lVGhhdFdvdWxkOnNvbWVTZXJ2aWNlS2V5', token)
