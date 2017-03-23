import json
from unittest import TestCase


class TestConfigTest(TestCase):

    @classmethod
    def setUpClass(cls):
        super(TestConfigTest, cls).setUpClass()
        with open('tests/test-config.json') as configuration_data:
            cls.data = json.load(configuration_data)

    def test_username_exists(self):
        self.assertIsNotNone(self.data['username'], 'Add a username to test-config.json')

    def test_api_key_exists(self):
        self.assertIsNotNone(self.data['api_key'], 'Add an api_key to test-config.json')

    def test_service_key_exists(self):
        self.assertIsNotNone(self.data['service_key'], 'Add a service_key to test-config.json')

    def test_not_localhost(self):
        self.assertFalse('localhost' in self.data['teamserver_url'], "Use 127.0.0.1 instead of localhost within test-config.json")

    def test_org_uuid_exists(self):
        self.assertIsNotNone(self.data['org_uuid'], 'Add an org_uuid to test-config.json')

    def test_server_id_exists(self):
        self.assertIsNotNone(self.data['server_id'], 'Add a server_id to test-config.json')

    def test_app_id_exists(self):
        self.assertIsNotNone(self.data['app_id'], 'Add an app_id to test-config.json')

    def test_trace_id_exists(self):
        self.assertIsNotNone(self.data['trace_id'], 'Add a trace_id to test-config.json')

    def test_java_library_hash_exists(self):
        self.assertIsNotNone(self.data['java_library_hash'], 'Add a java_library_hash to test-config.json')