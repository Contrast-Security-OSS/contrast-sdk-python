import json
from unittest import TestCase

from contrast_security.contrast_sdk import ContrastSdk


class RouteCoverageApiTest(TestCase):

    @classmethod
    def setUpClass(cls):
        super(RouteCoverageApiTest, cls).setUpClass()
        with open('tests/test-config.json') as configuration_data:
            cls.data = json.load(configuration_data)
        cls.sdk = ContrastSdk(cls.data['username'], cls.data['api_key'], cls.data['service_key'], cls.data['teamserver_url'])
        cls.org_uuid = cls.data['org_uuid']
        cls.app_id = cls.data['app_id']

    def get_route_status_test(self):
        self.assertEqual(200, self.sdk.get_route_status(self.org_uuid, self.app_id).status_code)

    def get_filter_route_test(self):
        self.assertEqual(200, self.sdk.filter_routes(self.org_uuid, self.app_id, metadata=[{'label': 'test_label', 'values': ['test1']}], sessionID='testSessionID').status_code)
