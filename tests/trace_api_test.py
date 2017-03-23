import json
from unittest import TestCase

from contrast_security.contrast_sdk import ContrastSdk


class TraceApiTest(TestCase):

    @classmethod
    def setUpClass(cls):
        super(TraceApiTest, cls).setUpClass()
        with open('tests/test-config.json') as configuration_data:
            cls.data = json.load(configuration_data)
        cls.sdk = ContrastSdk(cls.data['username'], cls.data['api_key'], cls.data['service_key'],cls.data['teamserver_url'])
        cls.org_uuid = cls.data['org_uuid']
        cls.app_id = cls.data['app_id']
        cls.trace_id = cls.data['trace_id']

    def filter_org_traces_test(self):
        self.assertEquals(200, self.sdk.filter_org_traces(self.org_uuid).status_code)

    def get_org_trace_test(self):
            self.assertEquals(200,self.sdk.get_org_trace(self.org_uuid, self.trace_id).status_code)

    def get_trace_notes_test(self):
        self.assertEquals(200, self.sdk.get_trace_notes(self.org_uuid, self.app_id, self.trace_id).status_code)

    def create_trace_note_test(self):
        self.assertEquals(200, self.sdk.create_trace_note(self.org_uuid, self.app_id, self.trace_id, 'A note').status_code)

    def get_org_trace_ids_test(self):
        self.assertEquals(200, self.sdk.get_org_trace_ids(self.org_uuid).status_code)

    def get_org_trace_policy_violations_test(self):
        self.assertEquals(200, self.sdk.get_org_trace_policy_violations(self.org_uuid).status_code)

    def get_trace_visibility_test(self):
        self.assertEquals(200, self.sdk.get_trace_visibility(self.org_uuid, self.trace_id).status_code)

    def get_new_trace_trend_test(self):
        self.assertEquals(200, self.sdk.get_new_trace_trend(self.org_uuid).status_code)

    def get_total_trace_trend_test(self):
        self.assertEquals(200, self.sdk.get_total_trace_trend(self.org_uuid).status_code)

    def get_trace_time_to_remediate_by_rule_test(self):
        self.assertEquals(200, self.sdk.get_trace_time_to_remediate_by_rule(self.org_uuid).status_code)

    def get_trace_time_to_remediate_by_severity_test(self):
        self.assertEquals(200, self.sdk.get_trace_time_to_remediate_by_severity(self.org_uuid).status_code)

    def get_trace_time_to_remediate_current_test(self):
        self.assertEquals(200, self.sdk.get_trace_time_to_remediate_current(self.org_uuid).status_code)

    def get_trace_time_to_remediate_month_trend_test(self):
        self.assertEquals(200, self.sdk.get_trace_time_to_remediate_month_trend(self.org_uuid).status_code)
