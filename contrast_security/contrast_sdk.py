from .user_api.util import Util
from .user_api.organization_api import _OrganizationApi
from .user_api.application_api import _ApplicationApi
from .user_api.server_api import _ServerApi
from .user_api.tags_api import _TagsApi
from .user_api.alerts_api import _AlertApi
from .user_api.events_api import _EventsApi
from .user_api.modules_api import _ModulesApi
from .user_api.library_api import _LibraryApi
from .user_api.scores_api import _ScoresApi
from .user_api.history_api import _HistoryApi
from .user_api.role_api import _RoleApi
from .user_api.profile_api import _ProfileApi
from .user_api.policy_api import _PolicyApi
from .user_api.agent_api import _AgentApi
from .user_api.webhook_api import _WebhookApi
from .user_api.user_api import _UserApi
from .user_api.trace_api import _TraceApi
from .user_api.route_coverage import _RouteCoverageApi
from .user_api.session_metadata_api import _SessionMetadataApi


class ContrastSdk(object):

    def __init__(self, username, api_key, service_key, teamserver_url='https://app.contrastsecurity.com'):
        self._username = username
        self._api_key = api_key
        self._service_key = service_key
        self._teamserver_url = teamserver_url

        self._setup_apis()

    def _configure_api_defaults(self, api_class):
        api_class._headers = self._create_headers()
        api_class._base_url = self._teamserver_url + '/Contrast/api'

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
        self._configure_tags_api()
        self._configure_alert_api()
        self._configure_events_api()
        self._configure_modules_api()
        self._configure_library_api()
        self._configure_scores_api()
        self._configure_history_api()
        self._configure_roles_api()
        self._configure_profile_api()
        self._configure_application_api()
        self._configure_policy_api()
        self._configure_agent_api()
        self._configure_user_api()
        self._configure_trace_api()
        self._configure_webhook_api()
        self._configure_route_coverage_api()

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

    def _configure_trace_api(self):
        self._traces = _TraceApi()
        self._configure_api_defaults(self._traces)
        self.filter_org_traces = self._traces.filter_org_traces
        self.get_org_trace = self._traces.get_org_trace
        self.get_trace_notes = self._traces.get_trace_notes
        self.create_trace_note = self._traces.create_trace_note
        self.get_org_trace_ids = self._traces.get_org_trace_ids
        self.get_org_trace_policy_violations = self._traces.get_org_trace_policy_violations
        self.get_trace_visibility = self._traces.get_trace_visibility
        self.get_new_trace_trend = self._traces.get_new_trace_trend
        self.get_total_trace_trend = self._traces.get_total_trace_trend
        self.get_trace_time_to_remediate_by_rule = self._traces.get_trace_time_to_remediate_by_rule
        self.get_trace_time_to_remediate_by_severity = self._traces.get_trace_time_to_remediate_by_severity
        self.get_trace_time_to_remediate_current = self._traces.get_trace_time_to_remediate_current
        self.get_trace_time_to_remediate_month_trend = self._traces.get_trace_time_to_remediate_month_trend
        self.get_trace_card = self._traces.get_trace_card
        self.get_trace_events_summary = self._traces.get_trace_events_summary
        self.get_trace_event_details = self._traces.get_trace_event_details
        self.get_trace_httprequest = self._traces.get_trace_httprequest
        self.get_trace_httprequest_details = self._traces.get_trace_httprequest_details
        self.get_trace_recommendation = self._traces.get_trace_recommendation
        self.get_trace_story = self._traces.get_trace_story

    def _configure_alert_api(self):
        self._alert = _AlertApi()
        self._configure_api_defaults(self._alert)
        self.get_alerts = self._alert.get_alerts
        self.get_alert_data = self._alert.get_alert_data

    def _configure_events_api(self):
        self._events = _EventsApi()
        self._configure_api_defaults(self._events)
        self.get_latest_events = self._events.get_latest_events
        self.get_latest_application_creation = self._events.get_latest_application_creation
        self.get_latest_server_creation = self._events.get_latest_server_creation
        self.get_latest_traces_received = self._events.get_latest_traces_received

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
        self._history = _HistoryApi()
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

    def _configure_policy_api(self):
        self._policy = _PolicyApi()
        self._configure_api_defaults(self._policy)
        self.get_validators_and_sanitizers = self._policy.get_validators_and_sanitizers
        self.get_validator_controls = self._policy.get_validator_controls
        self.get_sanitizer_controls = self._policy.get_sanitizer_controls
        self.get_control_suggestions = self._policy.get_control_suggestions

    def _configure_agent_api(self):
        self._agent = _AgentApi()
        self._configure_api_defaults(self._agent)
        self.get_agent_profiles = self._agent.get_agent_profiles
        self.get_agent_profile = self._agent.get_agent_profile
        self.get_agent_versions = self._agent.get_agent_versions
        self.download_agent = self._agent.download_agent

    def _configure_webhook_api(self):
        self._webhook = _WebhookApi()
        self._configure_api_defaults(self._webhook)
        self.get_webhooks = self._webhook.get_webhooks
        self.get_webhook = self._webhook.get_webhook

    def _configure_user_api(self):
        self._user = _UserApi()
        self._configure_api_defaults(self._user)
        self.get_users = self._user.get_users
        self.get_custom_alerts = self._user.get_custom_alerts
        self.get_custom_attack_alerts = self._user.get_custom_attack_alerts
        self.get_custom_vulnerability_alerts = self._user.get_custom_vulnerability_alerts
        self.get_user_information = self._user.get_user_information
        self.get_user_authorization_header = self._user.get_user_authorization_header

    def _configure_route_coverage_api(self):
        self._route_coverage = _RouteCoverageApi()
        self._configure_api_defaults(self._route_coverage)
        self.get_route_status = self._route_coverage.get_route_status
        self.filter_routes = self._route_coverage.filter_routes

    def _configure_session_metadata_api(self):
        self._session_metadata = _SessionMetadataApi()
        self._configure_api_defaults(self._session_metadata)
        self.filter_app_session_metadata = self._session_metadata.filter_app_session_metadata
