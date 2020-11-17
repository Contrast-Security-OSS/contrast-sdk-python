from .api_support import _ApiSupport


class _RouteCoverageApi(_ApiSupport):

    def __init__(self):
        super(_RouteCoverageApi, self).__init__()

    def get_route_status(self, org_uuid, app_id):
        path = '{org_uuid}/applications/{app_id}/route/status'.format(org_uuid=org_uuid, app_id=app_id)
        return self._get(path)

    def get_app_route_snapshot(self, org_uuid, app_id, start_date=None, end_date=None):
        """

        :param org_uuid: organization id
        :param app_id: application id
        :param start_date: int version of timestamp; Ex Jan 1, 2020 -> 1577854800
        :param end_date: int version of timestamp; Ex Jan 1, 2020 -> 1577854800
        :return: json of app route snapshot
        """
        path = '{org_uuid}/applications/{app_id}/route/snapshots'.format(org_uuid=org_uuid, app_id=app_id)
        return self._get(path, params={'startDate': start_date, 'endDate': end_date})

    def filter_routes(self, org_uuid, app_id, metadata=None, sessionID='', expand=None):
        """
        Metadata is a list of dicts containing a label and a list of values

        Example:

        metadata = [{'label': 'test_label', 'values': ['test_value_1']}]
        """
        if metadata is None:
            metadata = []
        path = '{org_uuid}/applications/{app_id}/route/filter'.format(org_uuid=org_uuid, app_id=app_id)
        return self._post(path, data={'metadata': metadata, 'sessionID': sessionID}, params={'expand': expand})
