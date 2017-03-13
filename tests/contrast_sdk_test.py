from unittest import TestCase

from lib.contrast.user_api.contrast_sdk import ContrastSdk


class ContrastSDKTest(TestCase):

    def sdk_creation_bad_url_test(self):
        try:
            ContrastSdk("contrast_admin", "api_key", "service_key", "http:19080/Contrast")
            assert False
        except ValueError:
            assert True


