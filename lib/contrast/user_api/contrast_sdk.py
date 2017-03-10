from util import Util
from organization_api import _OrganizationApi
from server_api import _ServerApi


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
        self._configure_server_api()

    def _configure_server_api(self):
        self._server = _ServerApi()
        self._configure_api_defaults(self._server)
        self.get_servers = self._server.get_servers
        self.get_active_servers = self._server.get_active_servers
        self.filter_servers = self._server.filter_servers
        self.get_server_filters = self._server.get_server_filters
        self.get_server_filter_subfilters = self._server.get_server_filter_subfilters
        self.get_server_modes = self._server.get_server_modes
        self.get_server_details = self._server.get_server_details
        self.get_server_activity = self._server.get_server_activity
        self.get_server_agent_activity = self._server.get_server_agent_activity
        self.get_server_attack_status = self._server.get_server_attack_status
        self.get_server_attack_types = self._server.get_server_attack_types
        self.get_server_trace_breakdown = self._server.get_server_trace_breakdown
        self.get_server_trace_severity_breakdown = self._server.get_server_trace_severity_breakdown
        self.get_server_trace_status_breakdwon = self._server.get_server_trace_status_breakdown
        self.get_server_libraries_breakdown = self._server.get_server_libraries_breakdown
        self.update_server_name = self._server.update_server_name
        self.get_server_properties = self._server.get_server_properties
        self.get_server_vuln_and_attack_urls = self._server.get_server_vuln_and_attack_urls
        self.get_server_vuln_urls = self._server.get_server_vuln_urls
        self.get_server_attack_urls = self._server.get_server_attack_urls
        self.get_server_libraries = self._server.get_server_libraries
        self.get_server_libraries_subfilters = self._server.get_server_libraries_subfilters
        self.filter_server_libraries = self._server.filter_server_libraries
        self.get_server_trace_subfilters = self._server.get_server_trace_subfilters
        self.get_server_trace_details = self._server.get_server_trace_details
        self.filter_server_traces = self._server.filter_server_traces
        self.delete_server_traces = self._server.delete_server_traces
        self.get_server_vulnerability_uuids = self._server.get_server_vulnerability_uuids
        self.get_server_policy_violations = self._server.get_server_policy_violations
        self.delete_server_trace = self._server.delete_server_trace
        self.get_server_trace_vulnerability = self._server.get_server_trace_vulnerability

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



