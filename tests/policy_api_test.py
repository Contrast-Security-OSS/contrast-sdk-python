import json
from unittest import TestCase

from contrast_security.contrast_sdk import ContrastSdk


class PolicyApiTest(TestCase):

    @classmethod
    def setUpClass(cls):
        super(PolicyApiTest, cls).setUpClass()
        with open('tests/test-config.json') as configuration_data:
            cls.data = json.load(configuration_data)
        cls.sdk = ContrastSdk(cls.data['username'], cls.data['api_key'], cls.data['service_key'],cls.data['teamserver_url'])
        cls.org_uuid = cls.data['org_uuid']

    def get_validators_and_sanitizers_test(self):
        self.assertEquals(200, self.sdk.get_validators_and_sanitizers(self.org_uuid).status_code)

    def get_validator_controls_test(self):
        self.assertEquals(200, self.sdk.get_validator_controls(self.org_uuid).status_code)

    def get_sanitizer_controls_test(self):
        self.assertEquals(200, self.sdk.get_sanitizer_controls(self.org_uuid).status_code)

    def get_control_suggestions_test(self):
        self.assertEquals(200, self.sdk.get_control_suggestions(self.org_uuid).status_code)
