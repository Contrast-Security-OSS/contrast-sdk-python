import json
from unittest import TestCase

from contrast_security.contrast_sdk import ContrastSdk


class ApplicationApiTest(TestCase):

    @classmethod
    def setUpClass(cls):
        super(ApplicationApiTest, cls).setUpClass()
        with open('tests/test-config.json') as configuration_data:
            cls.data = json.load(configuration_data)
        cls.sdk = ContrastSdk(cls.data['username'], cls.data['api_key'], cls.data['service_key'],cls.data['teamserver_url'])
        cls.org_uuid = cls.data['org_uuid']
        cls.app_id = cls.data['app_id']
        cls.trace_id = cls.data['trace_id']

    def inactive_apps_test(self):
        self.assertEqual(200, self.sdk.get_inactive_applications(self.org_uuid).status_code)

    def newest_apps_test(self):
        self.assertEqual(200, self.sdk.get_newest_applications(self.org_uuid).status_code)

    def recent_apps_test(self):
        self.assertEqual(200, self.sdk.get_recent_applications(self.org_uuid).status_code)

    def get_app_agent_activity_test(self):
        self.assertEqual(200, self.sdk.get_application_agent_activity(self.org_uuid,self.app_id,'months').status_code)

    def get_application_components_test(self):
        self.assertEqual(200, self.sdk.get_application_components(self.org_uuid, self.app_id).status_code)

    def get_application_coverage_test(self):
        self.assertEqual(200, self.sdk.get_application_coverage(self.org_uuid, self.app_id).status_code)

    def get_application_coverage_past_week_test(self):
        self.assertEqual(200, self.sdk.get_application_coverage_past_week(self.org_uuid, self.app_id).status_code)

    def get_application_history_test(self):
        self.assertEqual(200, self.sdk.get_application_history(self.org_uuid, self.app_id).status_code)

    def get_application_history_by_interval_test(self):
        self.assertEqual(200, self.sdk.get_application_history_by_interval(self.org_uuid, self.app_id).status_code)

    def get_application_libraries_test(self):
        self.assertEqual(200, self.sdk.get_application_libraries(self.org_uuid, self.app_id).status_code)

    def filter_application_libraries(self):
        self.assertEqual(200, self.sdk.filter_application_libraries(self.org_uuid, self.app_id).status_code)

    def get_application_library_subfilters_test(self):
        self.assertEqual(200, self.sdk.get_application_library_subfilters(self.org_uuid, self.app_id, 'tags').status_code)

    def get_application_libraries_stats_test(self):
        self.assertEqual(200, self.sdk.get_application_libraries_stats(self.org_uuid, self.app_id).status_code)

    def get_application_status_breakdown_test(self):
        self.assertEqual(200, self.sdk.get_application_status_breakdown(self.org_uuid, self.app_id).status_code)

    def get_application_trace_breakdown_test(self):
        self.assertEqual(200, self.sdk.get_application_trace_breakdown(self.org_uuid, self.app_id).status_code)

    def get_application_trace_rule_breakdown_test(self):
        self.assertEqual(200, self.sdk.get_application_trace_rule_breakdown(self.org_uuid, self.app_id).status_code)

    def get_application_trace_severity_breakdown_test(self):
        self.assertEqual(200, self.sdk.get_application_trace_severity_breakdown(self.org_uuid, self.app_id).status_code)

    def get_application_trace_status_breakdown_test(self):
        self.assertEqual(200, self.sdk.get_application_trace_status_breakdown(self.org_uuid, self.app_id).status_code)

    def get_application_servers(self):
        self.assertEqual(200, self.sdk.get_application_servers(self.org_uuid, self.app_id) .status_code)

    def get_application_servers_breakdown_test(self):
        self.assertEqual(200, self.sdk.get_application_servers_breakdown(self.org_uuid, self.app_id).status_code)

    def get_application_servers_count_test(self):
        self.assertEqual(200, self.sdk.get_application_servers_count(self.org_uuid, self.app_id).status_code)

    def get_application_servers_recently_active_test(self):
        self.assertEqual(200, self.sdk.get_application_servers_recently_active(self.org_uuid, self.app_id).status_code)

    def get_application_servers_properties_test(self):
        self.assertEqual(200, self.sdk.get_application_servers_properties(self.org_uuid, self.app_id).status_code)

    def get_application_servers_settings_test(self):
        self.assertEqual(200, self.sdk.get_application_servers_settings(self.org_uuid, self.app_id).status_code)

    def get_application_technologies_test(self):
        self.assertEqual(200, self.sdk.get_application_technologies(self.org_uuid, self.app_id).status_code)

    def get_technologies_test(self):
        self.assertEqual(200, self.sdk.get_technologies(self.org_uuid).status_code)

    def get_total_allowed_applications_test(self):
        self.assertEqual(200, self.sdk.get_total_allowed_applications(self.org_uuid).status_code)

    def filter_applications_test(self):
        self.assertEqual(200, self.sdk.filter_applications(self.org_uuid).status_code)

    def get_application_filters_test(self):
        self.assertEqual(200, self.sdk.get_application_filters(self.org_uuid) .status_code)

    def get_application_test(self):
        self.assertEqual(200, self.sdk.get_application(self.org_uuid, self.app_id).status_code)

    def update_application_importance_test(self):
        self.assertEqual(200, self.sdk.update_application_importance(self.org_uuid, self.app_id, 1).status_code)

    def get_application_license_details_test(self):
        self.assertEqual(200, self.sdk.get_application_license_details(self.org_uuid, self.app_id).status_code)

    def filter_app_traces_test(self):
        self.assertEqual(200, self.sdk.filter_application_traces(self.org_uuid, self.app_id).status_code)

    def get_application_vuln_details_test(self):
        self.assertEqual(200, self.sdk.get_application_vuln_details(self.org_uuid, self.app_id, self.trace_id).status_code)

    def get_application_traces_uuids_test(self):
        self.assertEqual(200, self.sdk.get_application_traces_uuids(self.org_uuid, self.app_id).status_code)

    def get_application_traces_with_policy_violations_test(self):
        self.assertEqual(200, self.sdk.get_application_traces_with_policy_violations(self.org_uuid, self.app_id).status_code)

    def get_application_trace_details_test(self):
        self.assertEqual(200, self.sdk.get_application_trace_details(self.org_uuid, self.app_id,self.trace_id).status_code)

    def get_application_trace_requirements_test(self):
        self.assertEqual(200, self.sdk.get_application_trace_requirements(self.org_uuid, self.app_id, self.trace_id).status_code)

    def get_application_trace_servers_test(self):
        self.assertEqual(200, self.sdk.get_application_trace_servers(self.org_uuid, self.app_id, self.trace_id).status_code)

    def get_application_trace_urls_test(self):
        self.assertEqual(200, self.sdk.get_application_trace_urls(self.org_uuid, self.app_id, self.trace_id).status_code)

    def get_application_trace_visibility_test(self):
        self.assertEqual(200, self.sdk.get_application_trace_visibility(self.org_uuid, self.app_id, self.trace_id).status_code)
