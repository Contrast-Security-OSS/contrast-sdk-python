from .api_support import _ApiSupport


class _ProfileApi(_ApiSupport):

    def __init__(self):
        super(_ProfileApi, self).__init__()

    def get_profile_info(self, expand=None):
        return self._get('profile', params=expand)

    def get_profile_organizations(self):
        return self._get('profile/organizations')

    def get_profile_default_organization(self):
        return self._get('profile/organizations/default')

    def get_org_info(self, org_uuid):
        path = 'profile/organizations/{org_uuid}'.format(org_uuid=org_uuid)
        return self._get(path)

    def get_profile_password_policy(self):
        return self._get('profile/passwordpolicy')

    def get_profile_roles(self):
        return self._get('profile/roles')

    def set_profile_default_org(self, org_uuid):
        path = 'profile/{org_uuid}/default'.format(org_uuid=org_uuid)
        return self._put(path)


