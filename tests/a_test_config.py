from unittest import TestCase
from lib.contrast.user_api.contrast_sdk import ContrastSdk
import json


class TestConfigTest(TestCase):

    @classmethod
    def setUpClass(cls):
        super(TestConfigTest, cls).setUpClass()
        with open('tests/test-config.json') as configuration_data:
            cls.data = json.load(configuration_data)

    def test_not_localhost(self):
        self.assertFalse('localhost' in self.data['teamserver_url'], "Use 127.0.0.1 instead of localhost within test-config.json")

    def test_org_uuid_exists(self):
        self.assertIsNotNone(self.data['org_uuid'], 'Add a org_uuid to test-config.json')

    def test_server_id_exists(self):
        self.assertIsNotNone(self.data['server_id'], 'Add a server_id to test-config.json')