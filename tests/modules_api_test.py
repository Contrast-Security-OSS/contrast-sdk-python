import json
from unittest import TestCase

from contrast_security.contrast_sdk import ContrastSdk


class ModulesApiTest(TestCase):

    @classmethod
    def setUpClass(cls):
        super(ModulesApiTest, cls).setUpClass()
        with open('tests/test-config.json') as configuration_data:
            cls.data = json.load(configuration_data)
        cls.sdk = ContrastSdk(cls.data['username'], cls.data['api_key'], cls.data['service_key'],cls.data['teamserver_url'])
        cls.org_uuid = cls.data['org_uuid']
        cls.master_app_id = cls.data['app_id']

    def get_modules_test(self):
        self.assertEquals(200, self.sdk.get_application_modules(self.org_uuid).status_code)

    def get_child_modules_test(self):
        self.assertEquals(200, self.sdk.get_application_child_modules(self.org_uuid, self.master_app_id).status_code)
