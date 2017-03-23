import json
from unittest import TestCase

from contrast_security.contrast_sdk import ContrastSdk


class HistoryApiTest(TestCase):

    @classmethod
    def setUpClass(cls):
        super(HistoryApiTest, cls).setUpClass()
        with open('tests/test-config.json') as configuration_data:
            cls.data = json.load(configuration_data)
        cls.sdk = ContrastSdk(cls.data['username'], cls.data['api_key'], cls.data['service_key'],cls.data['teamserver_url'])
        cls.org_uuid = cls.data['org_uuid']

    def history_limit_test(self):
        self.assertEquals(200, self.sdk.get_organization_score_history(self.org_uuid).status_code)

    def history_interval_test(self):
        self.assertEquals(200, self.sdk.get_organization_score_history_interval(self.org_uuid).status_code)
