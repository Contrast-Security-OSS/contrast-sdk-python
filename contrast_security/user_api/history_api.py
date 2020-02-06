from .api_support import _ApiSupport


class _HistoryApi(_ApiSupport):

    def __init__(self):
        super(_HistoryApi, self).__init__()

    def get_organization_score_history(self, org_uuid, limit=12):
        path = '{org_uuid}/history/scores'.format(org_uuid=org_uuid)
        return self._get(path, params={'limit': limit})

    def get_organization_score_history_interval(self, org_uuid, interval='WEEK', include_defense=False):
        defense_string = '/defense' if include_defense else ''
        path = '{org_uuid}/history/scores/interval{defense_string}'.format(org_uuid=org_uuid, defense_string=defense_string)
        return self._get(path, params={'interval': interval})