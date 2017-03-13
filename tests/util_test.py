from unittest import TestCase
from lib.contrast.user_api.util import Util


class UtilTest(TestCase):
    def create_auth_token_test(self):
        username = 'reallyLongUserNameThatWould'
        service_key = 'someServiceKey'
        token = Util.create_authorization_token(username, service_key)
        self.assertEqual('cmVhbGx5TG9uZ1VzZXJOYW1lVGhhdFdvdWxkOnNvbWVTZXJ2aWNlS2V5', token)

    def validate_url_failure_test(self):
        url = 'http//badurl.com'
        url2 = 'http://badurl'
        url3 = 'http:/badurl.com'
        self.assertFalse(Util.validate_url(url))
        self.assertFalse(Util.validate_url(url2))
        self.assertFalse(Util.validate_url(url3))

    def validate_url_success_test(self):
        url = 'http://verygoodurl.com'
        self.assertTrue(Util.validate_url(url))