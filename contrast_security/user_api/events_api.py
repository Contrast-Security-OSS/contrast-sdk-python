from .api_support import _ApiSupport


class _EventsApi(_ApiSupport):

    def __init__(self):
        super(_EventsApi, self).__init__()

    def get_latest_events(self, org_uuid, limit=10):
        path = '{org_uuid}/events'.format(org_uuid=org_uuid)
        return self._get(path, params={'limit': limit})

    def get_latest_application_creation(self, org_uuid, limit=10):
        path = '{org_uuid}/events/application'.format(org_uuid=org_uuid)
        return self._get(path, params={'limit': limit})

    def get_latest_server_creation(self, org_uuid, limit=10):
        path = '{org_uuid}/events/server'.format(org_uuid=org_uuid)
        return self._get(path, params={'limit': limit})

    def get_latest_traces_received(self, org_uuid, limit=10):
        path = '{org_uuid}/events/trace'.format(org_uuid=org_uuid)
        return self._get(path, params={'limit': limit})