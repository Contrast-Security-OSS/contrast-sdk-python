import json
from unittest import TestCase

from contrast_security.contrast_sdk import ContrastSdk


class RoleApiTest(TestCase):

    @classmethod
    def setUpClass(cls):
        super(RoleApiTest, cls).setUpClass()
        with open('tests/test-config.json') as configuration_data:
            cls.data = json.load(configuration_data)
        cls.sdk = ContrastSdk(cls.data['username'], cls.data['api_key'], cls.data['service_key'],cls.data['teamserver_url'])
        cls.org_uuid = cls.data['org_uuid']

    def org_info_test(self):
        self.assertEqual(200, self.sdk.get_roles().status_code)

