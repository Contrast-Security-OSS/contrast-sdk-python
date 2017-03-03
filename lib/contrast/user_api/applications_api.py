from api_support import _ApiSupport


class _ApplicationApi(_ApiSupport):

    def __init__(self):
        super(_ApplicationApi, self).__init__()

    def get_applications(self, org_uuid, params=None):
        path = '{org_uuid}/applications/filter'.format(org_uuid=org_uuid)
        return self._get(path, params=params)

