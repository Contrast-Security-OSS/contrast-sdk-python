from .api_support import _ApiSupport


class _RoleApi(_ApiSupport):

    def __init__(self):
        super(_RoleApi, self).__init__()

    def get_roles(self):
        return self._get('roles')


