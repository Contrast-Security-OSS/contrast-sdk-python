import json
from unittest import TestCase

from contrast_security.contrast_sdk import ContrastSdk


class OrganizationApiTest(TestCase):

    @classmethod
    def setUpClass(cls):
        super(OrganizationApiTest, cls).setUpClass()
        with open('tests/test-config.json') as configuration_data:
            cls.data = json.load(configuration_data)
        cls.sdk = ContrastSdk(cls.data['username'], cls.data['api_key'], cls.data['service_key'],cls.data['teamserver_url'])
        cls.org_uuid = cls.data['org_uuid']

    def org_info_test(self):
        self.assertEqual(200, self.sdk.get_organization_info(self.org_uuid).status_code)

    def org_search_test(self):
        self.assertEqual(200, self.sdk.search(self.org_uuid, 'a').status_code)

    def org_administrators_test(self):
        self.assertEqual(200, self.sdk.get_organization_administrators(self.org_uuid).status_code)

    def org_app_roles_test(self):
        self.assertEqual(200, self.sdk.get_organization_application_roles(self.org_uuid).status_code)

    def org_update_library_scoring_test(self):
        self.assertEqual(200, self.sdk. put_organization_library_scoring(self.org_uuid, scoring_type="DEFAULT").status_code)

    def org_library_scoring_test(self):
        self.assertEqual(200, self.sdk.get_organization_library_scoring(self.org_uuid).status_code)

    def org_server_restart_test(self):
        self.assertEqual(200, self.sdk.get_organization_servers_needing_restart(self.org_uuid, "Java").status_code)
        self.assertEqual(200, self.sdk.get_organization_servers_needing_restart(self.org_uuid, ".Net").status_code)
        self.assertEqual(200, self.sdk.get_organization_servers_needing_restart(self.org_uuid, "Node").status_code)

    def org_application_stats_test(self):
        self.assertEqual(200, self.sdk.get_organization_application_stats(self.org_uuid).status_code)

    def org_library_stats_test(self):
        self.assertEqual(200, self.sdk.get_organization_library_stats(self.org_uuid).status_code)

    def org_server_stats_test(self):
        self.assertEqual(200, self.sdk.get_organization_server_stats(self.org_uuid).status_code)

    def org_trace_stats_test(self):
        self.assertEqual(200, self.sdk.get_organization_trace_stats(self.org_uuid).status_code)

    def org_server_settings_test(self):
        self.assertEqual(200, self.sdk.get_organization_server_settings(self.org_uuid).status_code)


