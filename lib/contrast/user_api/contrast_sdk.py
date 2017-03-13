from util import Util
from organization_api import _OrganizationApi
from scores_api import _ScoresApi

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
        self._configure_scores_api()

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



