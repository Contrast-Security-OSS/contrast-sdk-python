from .api_support import _ApiSupport


class _AlertApi(_ApiSupport):

    def __init__(self):
        super(_AlertApi, self).__init__()

    def get_alerts(self, org_uuid):
        path = '{org_uuid}/alerts'.format(org_uuid=org_uuid)
        return self._get(path)

    def get_alert_data(self, org_uuid, alert_id):
        path = '{org_uuid}/alerts/{alert_id}'.format(org_uuid=org_uuid, alert_id=alert_id)
        return self._get(path)