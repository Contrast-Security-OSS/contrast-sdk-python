import json
from unittest import TestCase

from contrast_security.contrast_sdk import ContrastSdk


class ServerApiTest(TestCase):

    @classmethod
    def setUpClass(cls):
        super(ServerApiTest, cls).setUpClass()
        with open('tests/test-config.json') as configuration_data:
            cls.data = json.load(configuration_data)
        cls.sdk = ContrastSdk(cls.data['username'], cls.data['api_key'], cls.data['service_key'], cls.data['teamserver_url'])
        cls.org_uuid = cls.data['org_uuid']
        cls.server_id = cls.data['server_id']

    def get_servers_test(self):
        self.assertEquals(200, self.sdk.get_servers(self.org_uuid).status_code)

    def get_active_servers(self):
        self.assertEqual(200, self.sdk.get_active_servers(self.org_uuid).status_code)

    def get_filter_servers_test(self):
        self.assertEqual(200, self.sdk.filter_servers(self.org_uuid).status_code)

    def get_server_filters_test(self):
        self.assertEqual(200, self.sdk.get_server_filters(self.org_uuid).status_code)

    def get_server_subfilters_test(self):
        self.assertEqual(200, self.sdk.get_server_filter_subfilters(self.org_uuid, 'environment').status_code)

    def get_server_modes_test(self):
        self.assertEqual(200, self.sdk.get_server_modes(self.org_uuid).status_code)

    def get_server_details_test(self):
        self.assertEqual(200, self.sdk.get_server_details(self.org_uuid,self.server_id).status_code)

    def get_server_activity_test(self):
        self.assertEqual(200, self.sdk.get_server_activity(self.org_uuid, self.server_id).status_code)

    def get_server_agent_activity_test(self):
        self.assertEqual(200, self.sdk.get_server_agent_activity(self.org_uuid, self.server_id).status_code)

    def get_server_attack_status_test(self):
        self.assertEquals(200, self.sdk.get_server_attack_status(self.org_uuid, self.server_id).status_code)

    def get_server_attack_type_test(self):
        self.assertEquals(200, self.sdk.get_server_attack_types(self.org_uuid, self.server_id).status_code)

    def get_server_trace_breakdown_test(self):
        self.assertEquals(200, self.sdk.get_server_trace_breakdown(self.org_uuid, self.server_id).status_code)

    def get_server_trace_severity_breakdown_test(self):
        self.assertEquals(200, self.sdk.get_server_trace_severity_breakdown(self.org_uuid, self.server_id).status_code)

    def get_server_trace_status_breakdown_test(self):
        self.assertEquals(200, self.sdk.get_server_trace_status_breakdwon(self.org_uuid, self.server_id).status_code)

    def get_server_library_breakdown(self):
        self.assertEquals(200, self.sdk.get_server_libraries_breakdown(self.org_uuid, self.server_id).status_code)

    def update_server_name_test(self):
        self.assertEquals(200, self.sdk.update_server_name(self.org_uuid, self.server_id, 'python-sdk').status_code)

    def get_server_vuln_and_attack_urls_test(self):
        self.assertEquals(200, self.sdk.get_server_vuln_and_attack_urls(self.org_uuid, self.server_id).status_code)

    def get_server_properties_test(self):
        self.assertEquals(200, self.sdk.get_server_properties(self.org_uuid, self.server_id).status_code)

    def get_server_vuln_urls_test(self):
        self.assertEquals(200, self.sdk.get_server_vuln_urls(self.org_uuid, self.server_id).status_code)

    def get_server_attack_urls_test(self):
        self.assertEquals(200, self.sdk.get_server_attack_urls(self.org_uuid, self.server_id).status_code)

    def get_server_libraries_test(self):
        self.assertEquals(200, self.sdk.get_server_libraries(self.org_uuid, self.server_id).status_code)

    def get_server_libraries_subfilters_test(self):
        self.assertEquals(200, self.sdk.get_server_libraries_subfilters(self.org_uuid, self.server_id, 'apps').status_code)

    def filter_server_libraries_test(self):
        self.assertEquals(200, self.sdk.filter_server_libraries(self.org_uuid, self.server_id).status_code)

    def get_server_trace_subfilters_test(self):
        self.assertEquals(200, self.sdk.get_server_trace_subfilters(self.org_uuid, self.server_id, 'modules').status_code)

    def filter_server_traces_test(self):
        self.assertEquals(200, self.sdk.filter_server_traces(self.org_uuid, self.server_id).status_code)

    def delete_server_traces_test(self):
        try:
            self.assertEquals(200, self.sdk.delete_server_traces(self.org_uuid, self.server_id, []).status_code)
            assert False
        except BaseException:
            assert True

    def get_server_vulnerability_uuids_test(self):
        self.assertEquals(200, self.sdk.get_server_vulnerability_uuids(self.org_uuid, self.server_id).status_code)

    def get_server_policy_violations_test(self):
        self.assertEquals(200, self.sdk.get_server_policy_violations(self.org_uuid, self.server_id).status_code)


