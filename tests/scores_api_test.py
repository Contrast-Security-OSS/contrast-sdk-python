import json
from unittest import TestCase

from contrast_security.contrast_sdk import ContrastSdk


class ScoresApiTest(TestCase):

    @classmethod
    def setUpClass(cls):
        super(ScoresApiTest, cls).setUpClass()
        with open('tests/test-config.json') as configuration_data:
            cls.data = json.load(configuration_data)
        cls.sdk = ContrastSdk(cls.data['username'], cls.data['api_key'], cls.data['service_key'],cls.data['teamserver_url'])
        cls.org_uuid = cls.data['org_uuid']

    def get_scores_test(self):
        self.assertEqual(200, self.sdk.get_overall_scores(self.org_uuid).status_code)

    def get_score_server_breakdown_test(self):
        self.assertEqual(200, self.sdk.get_score_server_breakdown(self.org_uuid).status_code)

    def get_score_trace_rule_breakdown_test(self):
        self.assertEqual(200, self.sdk.get_score_trace_rule_breakdown(self.org_uuid).status_code)

    def get_score_trace_severity_breakdown_test(self):
        self.assertEqual(200, self.sdk.get_score_trace_severity_breakdown(self.org_uuid).status_code)

    def get_score_trace_status_breakdown_test(self):
        self.assertEqual(200, self.sdk.get_score_trace_status_breakdown(self.org_uuid).status_code)

    def get_score_platform_test(self):
        self.assertEqual(200, self.sdk.get_score_platform(self.org_uuid).status_code)

    def get_score_platform_include_defense_test(self):
        self.assertEqual(200, self.sdk.get_score_platform_include_defense(self.org_uuid).status_code)

    def get_score_security_test(self):
        self.assertEqual(200, self.sdk.get_score_security(self.org_uuid).status_code)

    def get_score_security_include_defense_test(self):
        self.assertEqual(200, self.sdk.get_score_security_include_defense(self.org_uuid).status_code)



