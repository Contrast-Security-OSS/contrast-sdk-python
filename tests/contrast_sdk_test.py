from unittest import TestCase
import json
from contrast_security.contrast_sdk import ContrastSdk


class ContrastSDKTest(TestCase):

    @classmethod
    def setUpClass(cls):
        super(ContrastSDKTest, cls).setUpClass()
        with open('tests/test-config.json') as configuration_data:
            cls.data = json.load(configuration_data)
        cls.sdk = ContrastSdk(cls.data['username'], cls.data['api_key'], cls.data['service_key'], 'some-invalid-url')
        cls.org_uuid = cls.data['org_uuid']

    def sdk_creation_bad_url_test(self):
        try:
            self.sdk.get_org_info(self.org_uuid)
            assert False
        except ValueError:
            assert True


