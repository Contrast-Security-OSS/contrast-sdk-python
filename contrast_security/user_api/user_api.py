from .api_support import _ApiSupport


class _UserApi(_ApiSupport):

    def __init__(self):
        super(_UserApi, self).__init__()

    def get_users(self, org_uuid, expand=None):
        path = '{org_uuid}/users'.format(org_uuid=org_uuid)
        return self._get(path, params={'expand': expand})

    def get_custom_alerts(self, org_uuid):
        path = '{org_uuid}/users/alerts/custom'.format(org_uuid=org_uuid)
        return self._get(path)

    def get_custom_attack_alerts(self, org_uuid):
        path = '{org_uuid}/users/alerts/custom/attacks'.format(org_uuid=org_uuid)
        return self._get(path)

    def get_custom_vulnerability_alerts(self, org_uuid):
        path = '{org_uuid}/users/alerts/custom/vulnerabilities'.format(org_uuid=org_uuid)
        return self._get(path)

    def get_user_information(self, org_uuid, user_id, expand=None):
        path = '{org_uuid}/users/{user_id}'.format(org_uuid=org_uuid, user_id=user_id)
        return self._get(path, params={'expand': expand})

    def get_user_authorization_header(self, org_uuid, user_id):
        path = '{org_uuid}/users/{user_id}/authorization'.format(org_uuid=org_uuid, user_id=user_id)
        return self._get(path)



