from .api_support import _ApiSupport
from ..filters.trace_filter import TraceFilter
from ..filters.trace_trend_filter import TraceTrendFilter
from ..filters.trace_time_to_remediate_filter import TraceTimeToRemediateFilter


class _TraceApi(_ApiSupport):

    def __init__(self):
        super(_TraceApi, self).__init__()

    def filter_org_traces(self, org_uuid, trace_filter=None):
        if trace_filter is None:
            trace_filter = TraceFilter()
        path = '{org_uuid}/orgtraces/filter'.format(org_uuid=org_uuid)
        return self._get(path, params=trace_filter.get_params_as_json())

    def get_org_trace(self, org_uuid, trace_id, expand=None):
        path = '{org_uuid}/orgtraces/filter/{trace_id}'.format(
            org_uuid=org_uuid,
            trace_id=trace_id
        )
        return self._get(path, params={'expand': expand})

    def get_trace_notes(self, org_uuid, app_id, trace_id):
        path = '{org_uuid}/applications/{app_id}/traces/{trace_id}/notes'.format(
            org_uuid=org_uuid,
            app_id=app_id,
            trace_id=trace_id
        )
        return self._get(path)

    def create_trace_note(self,org_uuid, app_id, trace_id, note):
        path = '{org_uuid}/applications/{app_id}/traces/{trace_id}/notes'.format(
            org_uuid=org_uuid,
            app_id=app_id,
            trace_id=trace_id
        )
        return self._post(path, data={'note': note})

    def get_org_trace_ids(self, org_uuid, trace_filter=None):
        if trace_filter is None:
            trace_filter = TraceFilter()
        path = '{org_uuid}/orgtraces/ids'.format(org_uuid=org_uuid)
        return self._get(path, params=trace_filter.get_params_as_json())

    def get_org_trace_policy_violations(self, org_uuid):
        path = '{org_uuid}/orgtraces/policy/violations'.format(org_uuid=org_uuid)
        return self._get(path)

    def get_trace_visibility(self, org_uuid, trace_id):
        path = '{org_uuid}/orgtraces/{trace_id}/visible'.format(
            org_uuid=org_uuid,
            trace_id=trace_id
        )
        return self._get(path)

    def get_new_trace_trend(self, org_uuid, interval='week', trace_trend_filter=None):
        if trace_trend_filter is None:
            trace_trend_filter = TraceTrendFilter()
        path = '{org_uuid}/orgtraces/stats/trend/{interval}/new'.format(
            org_uuid=org_uuid,
            interval=interval
        )
        return self._get(path, params=trace_trend_filter.get_params_as_json())

    def get_total_trace_trend(self, org_uuid, interval='week', trace_trend_filter=None):
        if trace_trend_filter is None:
            trace_trend_filter = TraceTrendFilter()
        path = '{org_uuid}/orgtraces/stats/trend/{interval}/total'.format(
            org_uuid=org_uuid,
            interval=interval
        )
        return self._get(path, params=trace_trend_filter.get_params_as_json())

    def get_trace_time_to_remediate_by_rule(self, org_uuid,trace_time_to_remediate_filter=None):
        if trace_time_to_remediate_filter is None:
            trace_time_to_remediate_filter = TraceTimeToRemediateFilter()
        path = '{org_uuid}/orgtraces/stats/ttr/rule'.format(org_uuid=org_uuid)
        return self._get(path, params=trace_time_to_remediate_filter.get_params_as_json())

    def get_trace_time_to_remediate_by_severity(self, org_uuid, trace_time_to_remediate_filter=None):
        if trace_time_to_remediate_filter is None:
            trace_time_to_remediate_filter = TraceTimeToRemediateFilter()
        path = '{org_uuid}/orgtraces/stats/ttr/severity'.format(org_uuid=org_uuid)
        return self._get(path, params=trace_time_to_remediate_filter.get_params_as_json())

    def get_trace_time_to_remediate_current(self, org_uuid):
        path = '{org_uuid}/orgtraces/stats/ttr/severity/current'.format(org_uuid=org_uuid)
        return self._get(path)

    def get_trace_time_to_remediate_month_trend(self, org_uuid):
        path = '{org_uuid}/orgtraces/stats/ttr/severity/trend'.format(org_uuid=org_uuid)
        return self._get(path)

    def get_trace_card(self, org_uuid, trace_uuid):
        path = '{org_uuid}/traces/{trace_uuid}/card'.format(
            org_uuid=org_uuid,
            trace_uuid=trace_uuid
        )
        return self._get(path)

    def get_trace_events_summary(self, org_uuid, trace_uuid):
        path = '{org_uuid}/traces/{trace_uuid}/events/summary'.format(
            org_uuid=org_uuid,
            trace_uuid=trace_uuid
        )
        return self._get(path)

    def get_trace_event_details(self, org_uuid, trace_uuid, event_id):
        path = '{org_uuid}/traces/{trace_uuid}/events/{event_id}/details'.format(
            org_uuid=org_uuid,
            trace_uuid=trace_uuid,
            event_id=event_id
        )
        return self._get(path)

    def get_trace_httprequest(self, org_uuid, trace_uuid):
        path = '{org_uuid}/traces/{trace_uuid}/httprequest'.format(
            org_uuid=org_uuid,
            trace_uuid=trace_uuid,
        )
        return self._get(path)

    def get_trace_httprequest_details(self, org_uuid, trace_uuid):
        path = '{org_uuid}/traces/{trace_uuid}/httprequest/details'.format(
            org_uuid=org_uuid,
            trace_uuid=trace_uuid,
        )
        return self._get(path)

    def get_trace_recommendation(self, org_uuid, trace_uuid):
        path = '{org_uuid}/traces/{trace_uuid}/recommendation'.format(
            org_uuid=org_uuid,
            trace_uuid=trace_uuid,
        )
        return self._get(path)

    def get_trace_story(self, org_uuid, trace_uuid):
        path = '{org_uuid}/traces/{trace_uuid}/story'.format(
            org_uuid=org_uuid,
            trace_uuid=trace_uuid,
        )
        return self._get(path)
