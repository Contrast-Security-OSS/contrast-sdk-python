import json
from unittest import TestCase

from contrast_security.contrast_sdk import ContrastSdk


class LibraryApiTest(TestCase):

    @classmethod
    def setUpClass(cls):
        super(LibraryApiTest, cls).setUpClass()
        with open('tests/test-config.json') as configuration_data:
            cls.data = json.load(configuration_data)
        cls.sdk = ContrastSdk(cls.data['username'], cls.data['api_key'], cls.data['service_key'],cls.data['teamserver_url'])
        cls.org_uuid = cls.data['org_uuid']
        cls.java_hash = cls.data['java_library_hash']

    def get_libraries_test(self):
        self.assertEquals(200, self.sdk.get_libraries(self.org_uuid).status_code)

    def get_java_library_test(self):
        self.assertEquals(200, self.sdk.get_java_library(self.org_uuid, self.java_hash) .status_code)

    def get_library_stats_test(self):
        self.assertEquals(200, self.sdk.get_library_stats(self.org_uuid).status_code)

    def get_library_filter_subfilters_test(self):
        self.assertEquals(200, self.sdk.get_library_filter_subfilters(self.org_uuid, 'apps').status_code)

    def filter_libraries_test(self):
        self.assertEquals(200, self.sdk.filter_libraries(self.org_uuid).status_code)

    def get_all_library_filters_test(self):
        self.assertEquals(200, self.sdk.get_all_library_filters('APPLICATION').status_code)

    def get_library_policy_test(self):
        self.assertEquals(200, self.sdk.get_library_policy(self.org_uuid).status_code)

