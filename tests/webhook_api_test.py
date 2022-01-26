import json
from unittest import TestCase

from contrast_security.contrast_sdk import ContrastSdk


class WebhookApiTest(TestCase):

    @classmethod
    def setUpClass(cls):
        super(WebhookApiTest, cls).setUpClass()
        with open('tests/test-config.json') as configuration_data:
            cls.data = json.load(configuration_data)
        cls.sdk = ContrastSdk(cls.data['username'], cls.data['api_key'], cls.data['service_key'],cls.data['teamserver_url'])
        cls.org_uuid = cls.data['org_uuid']
        cls.webhook_url = cls.data['org_uuid']

    def get_webhooks_test(self):
        print(self.sdk._api_key)
        print(self.sdk._service_key)
        print(self.sdk._create_headers())
        self.assertEqual(200, self.sdk.get_webhooks(self.org_uuid).status_code)
