from .api_support import _ApiSupport
from ..filters.application_library_filter import ApplicationLibraryFilter
from ..filters.application_filter import ApplicationFilter
from ..filters.application_trace_filter import ApplicationTraceFilter

class _ApplicationApi(_ApiSupport):

    def __init__(self):
        super(_ApplicationApi, self).__init__()

    # App Activity
    def get_inactive_applications(self, org_uuid, expand=None, include_archived=False, include_merged=False, limit=5):
        path = '{org_uuid}/applications/activity/inactive'.format(org_uuid=org_uuid)
        return self._get(path, params={'expand': expand, 'includeArchived': include_archived, 'includeMerged': include_merged, 'limit': limit})

    def get_newest_applications(self, org_uuid, expand=None, include_archived=False, include_merged=False, limit=5):
        path = '{org_uuid}/applications/activity/newest'.format(org_uuid=org_uuid)
        return self._get(path, params={'expand': expand, 'includeArchived': include_archived, 'includeMerged': include_merged, 'limit': limit})

    def get_recent_applications(self, org_uuid, expand=None, include_archived=False, include_merged=False, limit=5):
        path = '{org_uuid}/applications/activity/recent'.format(org_uuid=org_uuid)
        return self._get(path, params={'expand': expand, 'includeArchived': include_archived, 'includeMerged': include_merged, 'limit': limit})

    # App Agent Activity
    def get_application_agent_activity(self, org_uuid, app_id, range, include_merged=False):
        path = '{org_uuid}/applications/{app_id}/agent/activity/{range}'.format(org_uuid=org_uuid, app_id=app_id, range=range)
        return self._get(path, params={'includeMerged': include_merged})

    # App Components
    def get_application_components(self,org_uuid, app_id):
        path = '{org_uuid}/applications/{app_id}/components'.format(org_uuid=org_uuid, app_id=app_id)
        return self._get(path)

    # App Coverage
    def get_application_coverage(self,org_uuid, app_id, include_merged=True, limit=50):
        path = '{org_uuid}/applications/{app_id}/coverage'.format(org_uuid=org_uuid, app_id=app_id)
        return self._get(path, params={'includeMerged': include_merged, 'limit': limit})

    def get_application_coverage_past_week(self,org_uuid, app_id, include_merged=True, limit=50):
        path = '{org_uuid}/applications/{app_id}/coverage/stats/week'.format(org_uuid=org_uuid, app_id=app_id)
        return self._get(path, params={'includeMerged': include_merged, 'limit': limit})

    # App History
    def get_application_history(self, org_uuid, app_id, include_merged=True):
        path = '{org_uuid}/applications/{app_id}/history'.format(org_uuid=org_uuid, app_id=app_id)
        return self._get(path, params={'includeMerged': include_merged})

    def get_application_history_by_interval(self, org_uuid, app_id, environment='DEVELOPMENT', interval='WEEK', include_merged=True, include_defense=False):
        defense_string = '/defense' if include_defense else ''
        path = '{org_uuid}/applications/{app_id}/history/interval{defense_string}'.format(org_uuid=org_uuid, app_id=app_id, defense_string=defense_string)
        return self._get(path, params={'environment': environment, 'interval': interval, 'includeMerged': include_merged})

    # App libraries
    def get_application_libraries(self, org_uuid, app_id, expand=None, load_cve=False, quick_filter='ALL'):
        path = '{org_uuid}/applications/{app_id}/libraries'.format(org_uuid=org_uuid, app_id=app_id)
        return self._get(path, params={'expand': expand, 'loadCVE': load_cve, 'quickFilter': quick_filter})

    def filter_application_libraries(self, org_uuid, app_id, app_library_filter=None):
        if app_library_filter is None:
            app_library_filter = ApplicationLibraryFilter()
        path = '{org_uuid}/applications/{app_id}/libraries/filter'.format(org_uuid=org_uuid, app_id=app_id)
        return self._get(path, params=app_library_filter.get_params_as_json())

    def get_application_library_subfilters(self, org_uuid, app_id, libraries_filter_type):
        path = '{org_uuid}/applications/{app_id}/libraries/filters/{libraries_filter_type}/listing'.format(org_uuid=org_uuid, app_id=app_id, libraries_filter_type=libraries_filter_type)
        return self._get(path)

    def get_application_libraries_stats(self, org_uuid, app_id, include_merged=False):
        path = '{org_uuid}/applications/{app_id}/libraries/stats'.format(org_uuid=org_uuid, app_id=app_id)
        return self._get(path, params={'includeMerged': include_merged})

    # App Scores
    def get_application_status_breakdown(self, org_uuid, app_id, include_merged=True):
        path = '{org_uuid}/applications/{app_id}/breakdown/status'.format(org_uuid=org_uuid, app_id=app_id)
        return self._get(path, params={'includeMerged': include_merged})

    def get_application_trace_breakdown(self, org_uuid, app_id, include_merged=True):
        path = '{org_uuid}/applications/{app_id}/breakdown/trace'.format(org_uuid=org_uuid, app_id=app_id)
        return self._get(path, params={'includeMerged': include_merged})

    def get_application_trace_rule_breakdown(self, org_uuid, app_id, environment='DEVELOPMENT'):
        path = '{org_uuid}/applications/{app_id}/breakdown/trace/rule'.format(org_uuid=org_uuid, app_id=app_id)
        return self._get(path, params={'environment': environment})

    def get_application_trace_severity_breakdown(self, org_uuid, app_id, environment='DEVELOPMENT'):
        path = '{org_uuid}/applications/{app_id}/breakdown/status'.format(org_uuid=org_uuid, app_id=app_id)
        return self._get(path, params={'environment': environment})

    def get_application_trace_status_breakdown(self, org_uuid, app_id, environment='DEVELOPMENT'):
        path = '{org_uuid}/applications/{app_id}/breakdown/trace/status'.format(org_uuid=org_uuid, app_id=app_id)
        return self._get(path, params={'environment': environment})

    # App Servers
    def get_application_servers(self, org_uuid, app_id, expand=None, include_merged=True, only_licensed=False):
        path = '{org_uuid}/applications/{app_id}/servers'.format(org_uuid=org_uuid, app_id=app_id)
        return self._get(path, params={'expand': expand, 'includeMerged': include_merged, 'onlyLicensed': only_licensed})

    def get_application_servers_breakdown(self, org_uuid, app_id):
        path = '{org_uuid}/applications/{app_id}/servers/breakdown'.format(org_uuid=org_uuid, app_id=app_id)
        return self._get(path)

    def get_application_servers_count(self, org_uuid, app_id, include_merged=True):
        path = '{org_uuid}/applications/{app_id}/servers/count'.format(org_uuid=org_uuid, app_id=app_id)
        return self._get(path, params={'includeMerged': include_merged})

    def get_application_servers_recently_active(self, org_uuid, app_id, expand=None, include_merged=True):
        path = '{org_uuid}/applications/{app_id}/servers/newest'.format(org_uuid=org_uuid, app_id=app_id)
        return self._get(path, params={'expand': expand, 'includeMerged': include_merged})

    def get_application_servers_properties(self, org_uuid, app_id, include_merged=True):
        path = '{org_uuid}/applications/{app_id}/servers/properties'.format(org_uuid=org_uuid, app_id=app_id)
        return self._get(path, params={'includeMerged': include_merged})

    def get_application_servers_settings(self, org_uuid, app_id, include_merged=True, filter_environment=None):
        env_string = '/environment' if filter_environment is not None else ''
        path = '{org_uuid}/applications/{app_id}/servers/settings{env_string}'.format(org_uuid=org_uuid, app_id=app_id, env_string=env_string)
        return self._get(path, params={'includeMerged': include_merged, 'environment': filter_environment})

    # App Technologies
    def get_application_technologies(self, org_uuid, app_id):
        path = '{org_uuid}/applications/{app_id}/techs'.format(org_uuid=org_uuid, app_id=app_id)
        return self._get(path)

    # Techs
    def get_technologies(self, org_uuid):
        path = '{org_uuid}/techs'.format(org_uuid=org_uuid)
        return self._get(path)

    # Applications
    def get_total_allowed_applications(self, org_uuid):
        path = '{org_uuid}/applications/allowed'.format(org_uuid=org_uuid)
        return self._get(path)

    def filter_applications(self, org_uuid, application_filter=None):
        if application_filter is None:
            application_filter = ApplicationFilter()
        path = '{org_uuid}/applications/filter'.format(org_uuid=org_uuid)
        return self._get(path, params=application_filter.get_params_as_json())

    def get_application_filters(self, org_uuid):
        path = '{org_uuid}/applications/filters/listing'.format(org_uuid=org_uuid)
        return self._get(path)

    def get_application(self, org_uuid, app_id, expand=None, include_merged=True):
        path = '{org_uuid}/applications/{app_id}'.format(org_uuid=org_uuid, app_id=app_id)
        return self._get(path, params={'expand': expand, 'includeMerged': include_merged})

    def update_application_importance(self, org_uuid, app_id, importance):
        path = '{org_uuid}/applications/{app_id}/importance'.format(org_uuid=org_uuid, app_id=app_id)
        return self._put(path, data={'importance': importance})

    def get_application_license_details(self, org_uuid, app_id):
        path = '{org_uuid}/applications/{app_id}/license'.format(org_uuid=org_uuid, app_id=app_id)
        return self._get(path)

    # Application Trace Filtering
    def filter_application_traces(self, org_uuid, app_id, application_trace_filter=None):
        if application_trace_filter is None:
            application_trace_filter = ApplicationTraceFilter()
        path = '{org_uuid}/traces/{app_id}/filter'.format(org_uuid=org_uuid, app_id=app_id)
        return self._get(path, params=application_trace_filter.get_params_as_json())

    def get_application_vuln_details(self, org_uuid, app_id, trace_uuid, expand=None):
        path = '{org_uuid}/traces/{app_id}/filter/{trace_uuid}'.format(org_uuid=org_uuid, app_id=app_id, trace_uuid=trace_uuid)
        return self._get(path, params={'expand': expand})

    def get_application_traces_uuids(self, org_uuid, app_id, application_trace_filter=None):
        if application_trace_filter is None:
            application_trace_filter = ApplicationTraceFilter()
        path = '{org_uuid}/traces/{app_id}/ids'.format(org_uuid=org_uuid, app_id=app_id)
        return self._get(path, params=application_trace_filter.get_params_as_json())

    def get_application_traces_with_policy_violations(self, org_uuid, app_id, environment='DEVELOPMENT'):
        path = '{org_uuid}/traces/{app_id}/policy/violations'.format(org_uuid=org_uuid, app_id=app_id)
        return self._get(path, params={'environment': environment})

    def delete_application_trace(self, org_uuid, app_id, trace_id):
        path = '{org_uuid}/traces/{app_id}/trace/{trace_id}'.format(org_uuid=org_uuid, app_id=app_id, trace_id=trace_id)
        return self._delete(path)

    def delete_application_traces(self,org_uuid, app_id, trace_id_array):
        path = '{org_uuid}/traces/{app_id}'.format(org_uuid=org_uuid, app_id=app_id)
        return self._delete(path, data={'traces': trace_id_array})

    def get_application_trace_details(self, org_uuid, app_id, trace_id, expand=None):
        path = '{org_uuid}/traces/{app_id}/trace/{trace_id}'.format(org_uuid=org_uuid, app_id=app_id, trace_id=trace_id)
        return self._get(path, params={'expand': expand})

    def get_application_trace_requirements(self, org_uuid, app_id, trace_id, expand=None):
        path = '{org_uuid}/traces/{app_id}/trace/{trace_id}/requirements'.format(org_uuid=org_uuid, app_id=app_id, trace_id=trace_id)
        return self._get(path, params={'expand': expand})

    def get_application_trace_servers(self, org_uuid, app_id, trace_id, expand=None):
        path = '{org_uuid}/traces/{app_id}/trace/{trace_id}/servers'.format(org_uuid=org_uuid, app_id=app_id, trace_id=trace_id)
        return self._get(path, params={'expand': expand})

    def get_application_trace_urls(self, org_uuid, app_id, trace_id, expand=None):
        path = '{org_uuid}/traces/{app_id}/trace/{trace_id}/urlinstances'.format(org_uuid=org_uuid, app_id=app_id, trace_id=trace_id)
        return self._get(path, params={'expand': expand})

    def get_application_trace_visibility(self, org_uuid, app_id, trace_id):
        path = '{org_uuid}/traces/{app_id}/{trace_id}/visible'.format(org_uuid=org_uuid, app_id=app_id, trace_id=trace_id)
        return self._get(path)





