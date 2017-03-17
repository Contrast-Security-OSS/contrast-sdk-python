from unittest import TestCase
from lib.contrast.user_api.contrast_sdk import ContrastSdk
import json


class AlertApiTest(TestCase):

    @classmethod
    def setUpClass(cls):
        super(AlertApiTest, cls).setUpClass()
        with open('tests/test-config.json') as configuration_data:
            cls.data = json.load(configuration_data)
        cls.sdk = ContrastSdk(cls.data['username'], cls.data['api_key'], cls.data['service_key'],cls.data['teamserver_url'])
        cls.org_uuid = cls.data['org_uuid']

    def get_alerts_test(self):
        self.assertEquals(200, self.sdk.get_organization_info(self.org_uuid).status_code)
