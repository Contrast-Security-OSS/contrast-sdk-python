from util import Util
from organization_api import _OrganizationApi
from server_api import _ServerApi
from modules_api import _ModulesApi
from library_api import _LibraryApi
from scores_api import _ScoresApi
from history_api import _HistoryApi
from role_api import _RoleApi
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
        self._configure_server_api()
        self._configure_modules_api()
        self._configure_library_api()
        self._configure_scores_api()
        self._configure_history_api()
        self._configure_roles_api()
        self._configure_profile_api()

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

    def _configure_modules_api(self):
        self._modules = _ModulesApi()
        self._configure_api_defaults(self._modules)
        self.get_application_modules = self._modules.get_application_modules
        self.get_application_child_modules = self._modules.get_application_child_modules

    def _configure_history_api(self):
        self._history = _HistoryApi
        self._configure_api_defaults(self._history)
        self.get_organization_score_history = self._history.get_organization_score_history
        self.get_organization_score_history_interval = self._history.get_organization_score_history_interval

    def _configure_roles_api(self):
        self._roles = _RoleApi()
        self._configure_api_defaults(self._roles)
        self.get_roles = self._roles.get_roles

    def _configure_scores_api(self):
        self._scores = _ScoresApi()
        self._configure_api_defaults(self._scores)
        self.get_overall_scores = self._scores.get_overall_scores
        self.get_score_category_breakdown = self._scores.get_score_category_breakdown
        self.get_score_rule_breakdown = self._scores.get_score_rule_breakdown
        self.get_score_server_breakdown = self._scores.get_score_server_breakdown
        self.get_score_severity_breakdown = self._scores.get_score_severity_breakdown
        self.get_score_status_breakdown = self._scores.get_score_status_breakdown
        self.get_score_trace_rule_breakdown = self._scores.get_score_trace_rule_breakdown
        self.get_score_trace_severity_breakdown = self._scores.get_score_trace_severity_breakdown
        self.get_score_trace_status_breakdown = self._scores.get_score_trace_status_breakdown
        self.get_score_platform = self._scores.get_score_platform
        self.get_score_platform_include_defense = self._scores.get_score_platform_include_defense
        self.get_score_security = self._scores.get_score_security
        self.get_score_security_include_defense = self._scores.get_score_security_include_defense

    def _configure_library_api(self):
        self._library = _LibraryApi()
        self._configure_api_defaults(self._library)
        self.get_libraries = self._library.get_libraries
        self.get_dotnet_library = self._library.get_dotnet_library
        self.get_java_library = self._library.get_java_library
        self.get_library_stats = self._library.get_library_stats
        self.get_library_filter_subfilters = self._library.get_library_filter_subfilters
        self.filter_libraries = self._library.filter_libraries
        self.get_all_library_filters = self._library.get_all_library_filters
        self.get_library_policy = self._library.get_library_policy

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



