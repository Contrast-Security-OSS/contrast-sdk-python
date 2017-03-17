from unittest import TestCase
from lib.contrast.user_api.contrast_sdk import ContrastSdk
import json


class UserApiTest(TestCase):

    @classmethod
    def setUpClass(cls):
        super(UserApiTest, cls).setUpClass()
        with open('tests/test-config.json') as configuration_data:
            cls.data = json.load(configuration_data)
        cls.sdk = ContrastSdk(cls.data['username'], cls.data['api_key'], cls.data['service_key'],cls.data['teamserver_url'])
        cls.org_uuid = cls.data['org_uuid']

    def get_users_test(self):
        self.assertEquals(200, self.sdk.get_users(self.org_uuid).status_code)

    def get_custom_alerts_test(self):
        self.assertEquals(200, self.sdk.get_custom_alerts(self.org_uuid).status_code)

    def get_custom_attack_alerts_test(self):
        self.assertEquals(200, self.sdk.get_custom_attack_alerts(self.org_uuid).status_code)

    def get_custom_vulnerability_alerts_test(self):
        self.assertEquals(200, self.sdk.get_custom_vulnerability_alerts(self.org_uuid).status_code)

    def get_user_information_test(self):
        self.assertEquals(200, self.sdk.get_user_information(self.org_uuid, 'contrast_admin').status_code)

    def get_user_authorization_header_test(self):
        self.assertEquals(200, self.sdk.get_user_authorization_header(self.org_uuid, 'contrast_admin').status_code)
