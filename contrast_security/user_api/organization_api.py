from .api_support import _ApiSupport


class _OrganizationApi(_ApiSupport):

    def __init__(self):
        super(_OrganizationApi, self).__init__()

    def search(self, org_uuid, query_string):
        path = '{org_uuid}/search'.format(org_uuid=org_uuid)
        return self._get(path, params={'q': query_string})

    def get_organization_info(self, org_uuid, expand=None):
        path = '{org_uuid}/organizations'.format(org_uuid=org_uuid)
        return self._get(path, params={'expand': expand})

    def get_organization_administrators(self, org_uuid):
        path = '{org_uuid}/organizations/administrators'.format(org_uuid=org_uuid)
        return self._get(path)

    def get_organization_application_roles(self, org_uuid):
        path = '{org_uuid}/organizations/application/roles'.format(org_uuid=org_uuid)
        return self._get(path)

    def get_organization_library_scoring(self, org_uuid):
        path = '{org_uuid}/organizations/scoring/libraries'.format(org_uuid=org_uuid)
        return self._get(path)

    def put_organization_library_scoring(self, org_uuid, fail_libraries_policy=True, scoring_type=None):
        path = '{org_uuid}/organizations/scoring/libraries'.format(org_uuid=org_uuid)
        return self._put(path, data={'fail_libraries_policy': fail_libraries_policy, 'type': scoring_type})

    def get_organization_servers_needing_restart(self, org_uuid, language):
        path = '{org_uuid}/organizations/servers/restart/{language}'.format(org_uuid=org_uuid, language=language)
        return self._get(path)

    def get_organization_application_stats(self, org_uuid, interval='WEEK', expand=None):
        path = '{org_uuid}/organizations/stats/application'.format(org_uuid=org_uuid)
        return self._get(path, params={'interval': interval, 'expand': expand})

    def get_organization_library_stats(self, org_uuid, interval='WEEK', expand=None):
        path = '{org_uuid}/organizations/stats/library'.format(org_uuid=org_uuid)
        return self._get(path, params={'interval': interval, 'expand': expand})

    def get_organization_server_stats(self, org_uuid, interval='WEEK', expand=None):
        path = '{org_uuid}/organizations/stats/server'.format(org_uuid=org_uuid)
        return self._get(path, params={'interval': interval, 'expand': expand})

    def get_organization_trace_stats(self, org_uuid, interval='WEEK'):
        path = '{org_uuid}/organizations/stats/trace'.format(org_uuid=org_uuid)
        return self._get(path, params={'interval': interval})

    def get_organization_server_settings(self, org_uuid):
        path = '{org_uuid}/server/settings'.format(org_uuid=org_uuid)
        return self._get(path)



