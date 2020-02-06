from .api_support import _ApiSupport


class _ModulesApi(_ApiSupport):

    def __init__(self):
        super(_ModulesApi, self).__init__()

    def get_application_modules(self, org_uuid, expand=None):
        path = '{org_uuid}/modules'.format(org_uuid=org_uuid)
        return self._get(path, params={'expand': expand})

    def get_application_child_modules(self, org_uuid, app_id, expand=None):
        path = '{org_uuid}/modules/{app_id}'.format(org_uuid=org_uuid, app_id=app_id)
        return self._get(path, params={'expand': expand})
