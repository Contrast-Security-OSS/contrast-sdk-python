import json
from unittest import TestCase

from contrast_security.contrast_sdk import ContrastSdk


class SessionMetadataApiTest(TestCase):

    @classmethod
    def setUpClass(cls):
        super(SessionMetadataApiTest, cls).setUpClass()
        with open('tests/test-config.json') as configuration_data:
            cls.data = json.load(configuration_data)
        cls.sdk = ContrastSdk(cls.data['username'], cls.data['api_key'], cls.data['service_key'], cls.data['teamserver_url'])
        cls.org_uuid = cls.data['org_uuid']
        cls.app_id = cls.data['app_id']

    def filter_app_session_metadata_test(self):
        self.assertEqual(200, self.sdk.filter_app_session_metadata(self.org_uuid, self.app_id).status_code)

    def get_app_agentsessions(self):
        self.assertEqual(200, self.sdk.get_app_agentsessions(self.org_uuid, self.app_id).status_code)

    def get_app_session_metadata_latest(self):
        self.assertEqual(200, self.sdk.get_app_session_metadata_latest(self.org_uuid, self.app_id).status_code)

    def get_app_session_metadata_sessionid(self):
        self.assertEqual(200, self.sdk.get_app_session_metadata_sessionid(self.org_uuid, self.app_id, self.session_id).status_code)
