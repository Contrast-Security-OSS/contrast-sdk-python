from unittest import TestCase
from lib.contrast.user_api.contrast_sdk import ContrastSdk
import json


class TagsApiTest(TestCase):

    @classmethod
    def setUpClass(cls):
        super(TagsApiTest, cls).setUpClass()
        with open('tests/test-config.json') as configuration_data:
            cls.data = json.load(configuration_data)
        cls.sdk = ContrastSdk(cls.data['username'], cls.data['api_key'], cls.data['service_key'],cls.data['teamserver_url'])
        cls.org_uuid = cls.data['org_uuid']
        cls.server_id = cls.data['server_id']
        cls.app_id = cls.data['app_id']
        cls.library_hash = cls.data['library_hash']
        cls.trace_id = cls.data['trace_id']
        cls.tag_name = cls.data['tag_name']


    def get_application_tags_test(self):
        self.assertEquals(200, self.sdk.get_application_tags(self.org_uuid, self.app_id).status_code)

    def get_all_library_tags_test(self):
        self.assertEquals(200, self.sdk.get_all_library_tags(self.org_uuid).status_code)

    def get_all_application_tags_test(self):
        self.assertEquals(200, self.sdk.get_all_application_tags(self.org_uuid).status_code)

    def get_application_library_tags_test(self):
        self.assertEquals(200, self.sdk.get_application_library_tags(self.org_uuid, self.app_id).status_code)

    def get_library_tag_list_test(self):
        self.assertEquals(200, self.sdk.get_library_tag_list(self.org_uuid, self.library_hash).status_code)

    def get_server_tag_list_test(self):
        self.assertEquals(200, self.sdk.get_server_tag_list(self.org_uuid, self.server_id).status_code)

    def get_all_server_tags_test(self):
        self.assertEquals(200, self.sdk.get_all_server_tags(self.org_uuid).status_code)

    def get_all_trace_tags_test(self):
        self.assertEquals(200, self.sdk.get_all_trace_tags(self.org_uuid).status_code)

    def get_all_trace_tags_for_application_test(self):
        self.assertEquals(200, self.sdk.get_all_trace_tags_for_application(self.org_uuid, self.app_id).status_code)

    def get_all_trace_tags_for_servers_test(self):
        self.assertEquals(200, self.sdk.get_all_trace_tags_for_servers(self.org_uuid, self.server_id).status_code)

    def get_all_tags_for_trace_test(self):
        self.assertEquals(200, self.sdk.get_all_tags_for_trace(self.org_uuid, self.trace_id).status_code)

    def tag_application_test(self):
        self.assertEquals(200, self.sdk.tag_application(self.org_uuid, self.app_id, self.tag_name).status_code)

    def tag_library_test(self):
        self.assertEquals(200, self.sdk.tag_library(self.org_uuid, self.library_hash, self.tag_name).status_code)

    def tag_server_test(self):
        self.assertEquals(200, self.sdk.tag_server(self.org_uuid, self.server_id, self.tag_name).status_code)

    def tag_trace_test(self):
        self.assertEquals(200, self.sdk.tag_trace(self.org_uuid, self.trace_id, self.tag_name).status_code)

    def delete_tag_from_application_test(self):
        self.assertEquals(200, self.sdk.delete_tag_from_application(self.org_uuid, self.app_id, self.tag_name).status_code)

    def delete_tag_from_trace_test(self):
        self.assertEquals(200, self.sdk.delete_tag_from_trace(self.org_uuid, self.trace_id, self.tag_name).status_code)

    def delete_tag_from_server_test(self):
        self.assertEquals(200, self.sdk.delete_tag_from_server(self.org_uuid, self.server_id, self.tag_name).status_code)

    def delete_tag_from_library_test(self):
        self.assertEquals(200, self.sdk.delete_tag_from_library(self.org_uuid, self.library_hash, self.trace_id).status_code)

