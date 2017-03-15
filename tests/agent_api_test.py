from unittest import TestCase
from lib.contrast.user_api.contrast_sdk import ContrastSdk
import json
import os.path


class HistoryApiTest(TestCase):

    @classmethod
    def setUpClass(cls):
        super(HistoryApiTest, cls).setUpClass()
        with open('tests/test-config.json') as configuration_data:
            cls.data = json.load(configuration_data)
        cls.sdk = ContrastSdk(cls.data['username'], cls.data['api_key'], cls.data['service_key'],cls.data['teamserver_url'])
        cls.org_uuid = cls.data['org_uuid']

    def get_agent_profiles_test(self):
        self.assertEquals(200, self.sdk.get_agent_profiles(self.org_uuid).status_code)

    def get_agent_versions_test(self):
        self.assertEquals(200, self.sdk.get_agent_versions(self.org_uuid).status_code)

    def download_agent_test(self):
        self.assertEquals(200, self.sdk.download_agent(self.org_uuid, 'java').status_code)
        self.assertTrue(os.path.isfile('contrast.jar'))
        os.remove('contrast.jar')
