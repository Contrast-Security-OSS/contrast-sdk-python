from .api_support import _ApiSupport


class _RouteCoverageApi(_ApiSupport):

    def __init__(self):
        super(_RouteCoverageApi, self).__init__()

    def get_route_status(self, org_uuid, app_id):
        path = '{org_uuid}/applications/{app_id}/route/status'.format(org_uuid=org_uuid, app_id=app_id)
        return self._get(path)

    def filter_routes(self, org_uuid, app_id, metadata=[], sessionID='', expand=None):
        """
        Metadata is a list of dicts containing a label and a list of values

        Example:

        metadata = [{'label': 'test_label', 'values': ['test_value_1']}]
        """
        path = '{org_uuid}/applications/{app_id}/route/filter'.format(org_uuid=org_uuid, app_id=app_id)
        return self._post(path, data={'metadata': metadata, 'sessionID': sessionID}, params={'expand': expand})
