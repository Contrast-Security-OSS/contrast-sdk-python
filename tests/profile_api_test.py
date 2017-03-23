import json
from unittest import TestCase

from contrast_security.contrast_sdk import ContrastSdk


class ProfileApiTest(TestCase):

    @classmethod
    def setUpClass(cls):
        super(ProfileApiTest, cls).setUpClass()
        with open('tests/test-config.json') as configuration_data:
            cls.data = json.load(configuration_data)
        cls.sdk = ContrastSdk(cls.data['username'], cls.data['api_key'], cls.data['service_key'],cls.data['teamserver_url'])
        cls.org_uuid = cls.data['org_uuid']

    def profile_info_test(self):
        self.assertEquals(200, self.sdk.get_profile_info().status_code)

    def profile_org_test(self):
        self.assertEquals(200, self.sdk.get_profile_organizations().status_code)

    def profile_default_org_test(self):
        self.assertEquals(200, self.sdk.get_profile_default_organization().status_code)

    def profile_org_info_test(self):
        self.assertEquals(200, self.sdk.get_org_info(self.org_uuid).status_code)

    def profile_password_policy_test(self):
        self.assertEquals(200, self.sdk.get_profile_password_policy().status_code)

    def profile_roles_test(self):
        self.assertEquals(200, self.sdk.get_profile_roles().status_code)

    def profile_default_org_set_test(self):
        self.assertEqual(200, self.sdk.set_profile_default_org(self.org_uuid).status_code)


