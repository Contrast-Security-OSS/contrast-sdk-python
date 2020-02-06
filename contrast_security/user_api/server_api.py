from .api_support import _ApiSupport
from ..filters.server_filter import ServerFilter
from ..filters.server_library_filter import ServerLibraryFilter
from ..filters.server_trace_filter import ServerTraceFilter


class _ServerApi(_ApiSupport):

    def __init__(self):
        super(_ServerApi, self).__init__()

    def get_servers(self, org_uuid, include_archived=False, expand=None, query=None):
        path = '{org_uuid}/servers'.format(org_uuid=org_uuid)
        return self._get(path, params={'q': query, 'includeArchived': include_archived, 'expand': expand})

    def get_active_servers(self, org_uuid):
        path = '{org_uuid}/servers/active'.format(org_uuid=org_uuid)
        return self._get(path)

    def filter_servers(self, org_uuid, server_filter=None):
        if server_filter is None:
            server_filter = ServerFilter()
        path = '{org_uuid}/servers/filter'.format(org_uuid=org_uuid)
        return self._get(path, params=server_filter.get_params_as_json())

    def get_server_filters(self, org_uuid):
        path = '{org_uuid}/servers/filters/listing'.format(org_uuid=org_uuid)
        return self._get(path)

    def get_server_filter_subfilters(self, org_uuid, filter_type):
        path = '{org_uuid}/servers/filters/{filter_type}/listing'.format(org_uuid=org_uuid, filter_type=filter_type)
        return self._get(path)

    def get_server_modes(self, org_uuid):
        path = '{org_uuid}/servers/modes'.format(org_uuid=org_uuid)
        return self._get(path)

    def get_server_details(self, org_uuid, server_id, expand=None):
        path = '{org_uuid}/servers/{server_id}'.format(org_uuid=org_uuid, server_id=server_id)
        return self._get(path, params={'expand': expand})

    def get_server_activity(self, org_uuid, server_id, start_date=None, end_date=None):
        path = '{org_uuid}/servers/{server_id}/activity'.format(org_uuid=org_uuid, server_id=server_id)
        return self._get(path, params={'startDate': start_date, 'endDate': end_date})

    def get_server_agent_activity(self, org_uuid, server_id, interval='WEEK'):
        path = '{org_uuid}/servers/{server_id}/activity/interval'.format(org_uuid=org_uuid, server_id=server_id)
        return self._get(path, params={'interval': interval})

    def get_server_app_traces(self, org_uuid, server_id, orphans=False):
        path = '{org_uuid}/servers/{server_id}/apptraces'.format(org_uuid=org_uuid, server_id=server_id)
        return self._get(path, params={'orphans': orphans})

    def get_server_attack_status(self, org_uuid, server_id, include_merged=True):
        path = '{org_uuid}/servers/{server_id}/breakdown/attack/status'.format(org_uuid=org_uuid, server_id=server_id)
        return self._get(path, params={'includeMerged': include_merged})

    def get_server_attack_types(self, org_uuid, server_id, include_merged=True):
        path = '{org_uuid}/servers/{server_id}/breakdown/attack/type'.format(org_uuid=org_uuid, server_id=server_id)
        return self._get(path, params={'includeMerged': include_merged})

    def get_server_trace_breakdown(self, org_uuid, server_id, include_merged=True):
        path = '{org_uuid}/servers/{server_id}/breakdown/trace/rule'.format(org_uuid=org_uuid, server_id=server_id)
        return self._get(path, params={'includeMerged': include_merged})

    def get_server_trace_severity_breakdown(self, org_uuid, server_id, include_merged=True):
        path = '{org_uuid}/servers/{server_id}/breakdown/trace/severity'.format(org_uuid=org_uuid, server_id=server_id)
        return self._get(path, params={'includeMerged': include_merged})

    def get_server_trace_status_breakdown(self, org_uuid, server_id, include_merged=True):
        path = '{org_uuid}/servers/{server_id}/breakdown/trace/status'.format(org_uuid=org_uuid, server_id=server_id)
        return self._get(path, params={'includeMerged': include_merged})

    def get_server_libraries_breakdown(self, org_uuid, server_id, include_merged=True, include_archived=False):
        path = '{org_uuid}/servers/{server_id}/libraries/breakdown'.format(org_uuid=org_uuid, server_id=server_id)
        return self._get(path, params={'includeMerged': include_merged, 'includeArchived': include_archived})

    def update_server_name(self, org_uuid, server_id, new_name):
        path = '{org_uuid}/servers/{server_id}/name'.format(org_uuid=org_uuid, server_id=server_id)
        return self._put(path, data={'name': new_name})

    def get_server_properties(self, org_uuid, server_id):
        path = '{org_uuid}/servers/{server_id}/properties'.format(org_uuid=org_uuid, server_id=server_id)
        return self._get(path)

    def get_server_vuln_and_attack_urls(self, org_uuid, server_id, interval='WEEK'):
        path = '{org_uuid}/servers/{server_id}/url'.format(org_uuid=org_uuid, server_id=server_id)
        return self._get(path, params={'interval': interval})

    def get_server_vuln_urls(self, org_uuid, server_id, interval='WEEK'):
        path = '{org_uuid}/servers/{server_id}/url/vuln'.format(org_uuid=org_uuid, server_id=server_id)
        return self._get(path, params={'interval': interval})

    def get_server_attack_urls(self, org_uuid, server_id, interval='WEEK'):
        path = '{org_uuid}/servers/{server_id}/url/attack'.format(org_uuid=org_uuid, server_id=server_id)
        return self._get(path, params={'interval': interval})

    def get_server_libraries(self, org_uuid, server_id, expand=None, quick_filter='ALL'):
        path = '{org_uuid}/servers/{server_id}/libraries'.format(org_uuid=org_uuid, server_id=server_id)
        return self._get(path, params={'expand': expand, 'quickFilter': quick_filter})

    def get_server_libraries_subfilters(self, org_uuid, server_id, libraries_filter_type):
        path = '{org_uuid}/servers/{server_id}/libraries/filters/{libraries_filter_type}/listing'.format(org_uuid=org_uuid, server_id=server_id, libraries_filter_type=libraries_filter_type)
        return self._get(path)

    def get_server_libraries_stats(self, org_uuid, server_id, include_merged=True):
        path = '{org_uuid}/servers/{server_id}/libraries/stats'.format(org_uuid=org_uuid, server_id=server_id)
        return self._get(path, params={'includeMerged': include_merged})

    def filter_server_libraries(self, org_uuid, server_id, server_library_filter=None):
        if server_library_filter is None:
            server_library_filter = ServerLibraryFilter()
        path = '{org_uuid}/servers/{server_id}/libraries/filter'.format(org_uuid=org_uuid, server_id=server_id)
        return self._get(path, params=server_library_filter.get_params_as_json())

    def get_server_trace_subfilters(self, org_uuid, server_id, trace_filter_type):
        path = '{org_uuid}/servertraces/{server_id}/filter/{trace_filter_type}/listing'.format(org_uuid=org_uuid, server_id=server_id, trace_filter_type=trace_filter_type)
        return self._get(path)

    def get_server_trace_details(self, org_uuid, server_id, trace_uuid, expand=None):
        path = '{org_uuid}/servertraces/{server_id}/filter/{trace_uuid}'.format(org_uuid=org_uuid, server_id=server_id, trace_uuid=trace_uuid)
        return self._get(path, params={'expand': expand})

    def filter_server_traces(self, org_uuid, server_id, server_trace_filter=None):
        if server_trace_filter is None:
            server_trace_filter = ServerTraceFilter()
        path = '{org_uuid}/servertraces/{server_id}/filter'.format(org_uuid=org_uuid, server_id=server_id)
        return self._get(path, params=server_trace_filter.get_params_as_json())

    def delete_server_traces(self, org_uuid, server_id, traces=[]):
        if len(traces) < 1:
            raise BaseException('Trace list cannot be empty')
        path = '{org_uuid}/servertraces/{server_id}'.format(org_uuid=org_uuid, server_id=server_id)
        return self._delete(path, data={'traces': traces})

    def get_server_vulnerability_uuids(self, org_uuid, server_id, server_trace_filter=None):
        if server_trace_filter is None:
            server_trace_filter = ServerTraceFilter()
        path = '{org_uuid}/servertraces/{server_id}/ids'.format(org_uuid=org_uuid, server_id=server_id)
        return self._get(path, params=server_trace_filter.get_params_as_json())

    def get_server_policy_violations(self, org_uuid, server_id):
        path = '{org_uuid}/servertraces/{server_id}/policy/violations'.format(org_uuid=org_uuid, server_id=server_id)
        return self._get(path)

    def delete_server_trace(self, org_uuid, server_id, trace_uuid):
        path = '{org_uuid}/servertraces/{server_id}/trace/{trace_uuid}'.format(org_uuid=org_uuid, server_id=server_id, trace_uuid=trace_uuid)
        return self._get(path)

    def get_server_trace_vulnerability(self, org_uuid, server_id, trace_uuid):
        path = '{org_uuid}/servertraces/{server_id}/{trace_uuid}/visible'.format(org_uuid=org_uuid, server_id=server_id, trace_uuid=trace_uuid)
        return self._get(path);