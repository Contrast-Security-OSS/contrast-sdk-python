from util import Util
from organization_api import _OrganizationApi
from tags_api import _TagsApi
from profile_api import _ProfileApi

class ContrastSdk(object):

    def __init__(self, username, api_key, service_key, teamserver_url='https://app.contrastsecurity.com/Contrast'):

        if not Util.validate_url(teamserver_url):
            raise ValueError('Invalid Url')

        self._username = username
        self._api_key = api_key
        self._service_key = service_key
        self._teamserver_url = teamserver_url

        self._setup_apis()

    def _configure_api_defaults(self, api_class):
        api_class._headers = self._create_headers()
        api_class._base_url = self._teamserver_url + '/api'

    def _create_headers(self):
        return {
                    'Authorization': Util.create_authorization_token(self._username, self._service_key),
                    'API-Key': self._api_key,
                    'Content-type': 'application/json',
                    'Accept': 'application/json'
                }

    def _setup_apis(self):
        self._configure_organization_api()
        self._configure_tags_api()
        self._configure_profile_api()

    def _configure_tags_api(self):
        self._tags = _TagsApi()
        self._configure_api_defaults(self._tags)
        self.get_application_tags = self._tags.get_application_tags
        self.get_all_library_tags = self._tags.get_all_library_tags
        self.get_all_application_tags = self._tags.get_all_application_tags
        self.get_application_library_tags = self._tags.get_application_library_tags
        self.get_library_tag_list = self._tags.get_library_tag_list
        self.get_server_tag_list = self._tags.get_server_tag_list
        self.get_all_server_tags = self._tags.get_all_server_tags
        self.get_all_trace_tags = self._tags.get_all_trace_tags
        self.get_all_trace_tags_for_application = self._tags.get_all_trace_tags_for_application
        self.get_all_trace_tags_for_servers = self._tags.get_all_trace_tags_for_servers
        self.get_all_tags_for_trace = self._tags.get_all_tags_for_trace
        self.tag_application = self._tags.tag_application
        self.tag_library = self._tags.tag_library
        self.tag_server = self._tags.tag_server
        self.tag_trace = self._tags.tag_trace
        self.delete_tag_from_application = self._tags.delete_tag_from_application
        self.delete_tag_from_trace = self._tags.delete_tag_from_trace
        self.delete_tag_from_server = self._tags.delete_tag_from_server
        self.delete_tag_from_library = self._tags.delete_tag_from_library


    def _configure_profile_api(self):
        self._profile = _ProfileApi()
        self._configure_api_defaults(self._profile)
        self.get_profile_info = self._profile.get_profile_info
        self.get_profile_organizations = self._profile.get_profile_organizations
        self.get_profile_default_organization = self._profile.get_profile_default_organization
        self.get_org_info = self._profile.get_org_info
        self.get_profile_password_policy = self._profile.get_profile_password_policy
        self.get_profile_roles = self._profile.get_profile_roles
        self.set_profile_default_org = self._profile.set_profile_default_org

    def _configure_organization_api(self):
        self._organization = _OrganizationApi()
        self._configure_api_defaults(self._organization)
        self.search = self._organization.search
        self.get_organization_info = self._organization.get_organization_info
        self.get_organization_administrators = self._organization.get_organization_administrators
        self.get_organization_application_roles = self._organization.get_organization_application_roles
        self.get_organization_library_scoring = self._organization.get_organization_library_scoring
        self.put_organization_library_scoring = self._organization.put_organization_library_scoring
        self.get_organization_servers_needing_restart = self._organization.get_organization_servers_needing_restart
        self.get_organization_application_stats = self._organization.get_organization_application_stats
        self.get_organization_server_stats = self._organization.get_organization_server_stats
        self.get_organization_library_stats = self._organization.get_organization_library_stats
        self.get_organization_trace_stats = self._organization.get_organization_trace_stats
        self.get_organization_server_settings = self._organization.get_organization_server_settings



