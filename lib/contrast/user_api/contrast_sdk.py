from util import Util
from organization_api import _OrganizationApi
from application_api import _ApplicationApi
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
        self._configure_profile_api()
        self._configure_application_api()

    def _configure_application_api(self):
        self._applications = _ApplicationApi()
        self._configure_api_defaults(self._applications)
        self.get_inactive_applications = self._applications.get_inactive_applications
        self.get_newest_applications = self._applications.get_newest_applications
        self.get_recent_applications = self._applications.get_recent_applications
        self.get_application_agent_activity = self._applications.get_application_agent_activity
        self.get_application_components = self._applications.get_application_components
        self.get_application_coverage = self._applications.get_application_coverage
        self.get_application_coverage_past_week = self._applications.get_application_coverage_past_week
        self.get_application_history = self._applications.get_application_history
        self.get_application_history_by_interval = self._applications.get_application_history_by_interval
        self.get_application_libraries = self._applications.get_application_libraries
        self.filter_application_libraries = self._applications.filter_application_libraries
        self.get_application_library_subfilters = self._applications.get_application_library_subfilters
        self.get_application_libraries_stats = self._applications.get_application_libraries_stats
        self.get_application_status_breakdown = self._applications.get_application_status_breakdown
        self.get_application_trace_breakdown = self._applications.get_application_trace_breakdown
        self.get_application_trace_rule_breakdown = self._applications.get_application_trace_rule_breakdown
        self.get_application_trace_severity_breakdown = self._applications.get_application_trace_severity_breakdown
        self.get_application_trace_status_breakdown = self._applications.get_application_trace_status_breakdown
        self.get_application_servers = self._applications.get_application_servers
        self.get_application_servers_breakdown = self._applications.get_application_servers_breakdown
        self.get_application_servers_count = self._applications.get_application_servers_count
        self.get_application_servers_recently_active = self._applications.get_application_servers_recently_active
        self.get_application_servers_properties = self._applications.get_application_servers_properties
        self.get_application_servers_settings = self._applications.get_application_servers_settings
        self.get_application_technologies = self._applications.get_application_technologies
        self.get_technologies = self._applications.get_technologies
        self.get_total_allowed_applications = self._applications.get_total_allowed_applications
        self.filter_applications = self._applications.filter_applications
        self.get_application_filters = self._applications.get_application_filters
        self.get_application = self._applications.get_application
        self.update_application_importance = self._applications.update_application_importance
        self.get_application_license_details = self._applications.get_application_license_details
        self.filter_application_traces = self._applications.filter_application_traces
        self.get_application_vuln_details = self._applications.get_application_vuln_details
        self.get_application_traces_uuids = self._applications.get_application_traces_uuids
        self.get_application_traces_with_policy_violations = self._applications.get_application_traces_with_policy_violations
        self.delete_application_trace = self._applications.delete_application_trace
        self.delete_application_traces = self._applications.delete_application_traces
        self.get_application_trace_details = self._applications.get_application_trace_details
        self.get_application_trace_requirements = self._applications.get_application_trace_requirements
        self.get_application_trace_servers = self._applications.get_application_trace_servers
        self.get_application_trace_urls = self._applications.get_application_trace_urls
        self.get_application_trace_visibility = self._applications.get_application_trace_visibility

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



