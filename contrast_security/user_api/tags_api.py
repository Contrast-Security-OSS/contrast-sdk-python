from .api_support import _ApiSupport


class _TagsApi(_ApiSupport):

    def __init__(self):
        super(_TagsApi, self).__init__()

    def get_application_tags(self, org_uuid, app_id):
        path = '{org_uuid}/tags/application/list/{app_id}'.format(org_uuid=org_uuid, app_id=app_id)
        return self._get(path)

    def get_all_library_tags(self, org_uuid):
        path = '{org_uuid}/tags/libraries/list'.format(org_uuid=org_uuid)
        return self._get(path)

    def get_all_application_tags(self, org_uuid):
        path = '{org_uuid}/tags/applications/list'.format(org_uuid=org_uuid)
        return self._get(path)

    def get_application_library_tags(self, org_uuid, app_id):
        path = '{org_uuid}/tags/libraries/{app_id}/list'.format(org_uuid=org_uuid, app_id=app_id)
        return self._get(path)

    def get_library_tag_list(self, org_uuid, library_hash):
        path = '{org_uuid}/tags/library/list/{library_hash}'.format(org_uuid=org_uuid, library_hash=library_hash)
        return self._get(path)

    def get_server_tag_list(self, org_uuid, server_id):
        path = '{org_uuid}/tags/server/list/{server_id}'.format(org_uuid=org_uuid, server_id=server_id)
        return self._get(path)

    def get_all_server_tags(self, org_uuid):
        path = '{org_uuid}/tags/servers/list'.format(org_uuid=org_uuid)
        return self._get(path)

    def get_all_trace_tags(self, org_uuid):
        path = '{org_uuid}/tags/traces'.format(org_uuid=org_uuid)
        return self._get(path)

    def get_all_trace_tags_for_application(self, org_uuid, app_id):
        path = '{org_uuid}/tags/traces/application/{app_id}'.format(org_uuid=org_uuid, app_id=app_id)
        return self._get(path)

    def get_all_trace_tags_for_servers(self, org_uuid, server_id):
        path = '{org_uuid}/tags/traces/server/{server_id}'.format(org_uuid=org_uuid, server_id=server_id)
        return self._get(path)

    def get_all_tags_for_trace(self, org_uuid, trace_id):
        path = '{org_uuid}/tags/traces/trace/{trace_id}'.format(org_uuid=org_uuid, trace_id=trace_id)
        return self._get(path)

    def tag_application(self, org_uuid, app_id, tag_name):
        path = '{org_uuid}/tags/applications'.format(org_uuid=org_uuid)
        return self._put(path, data={"applications_id": [app_id], 'links': [], 'tags': [tag_name]})

    def tag_library(self, org_uuid, library, tag_name):
        path = '{org_uuid}/tags/libraries'.format(org_uuid=org_uuid)
        return self._put(path, data={'libraries': [library], 'links': [], 'tags': [tag_name]})

    def tag_server(self, org_uuid, server_id, tag_name):
        path = '{org_uuid}/tags/servers'.format(org_uuid=org_uuid)
        return self._put(path, data={'servers_id': [server_id], 'links': [], 'tags': [tag_name]})

    def tag_trace(self, org_uuid, trace_id, tag_name):
        path = '{org_uuid}/tags/traces'.format(org_uuid=org_uuid)
        return self._put(path, data={'traces_id': [trace_id], 'links': [], 'tags': [tag_name]})

    def delete_tag_from_application(self, org_uuid, app_id, tag):
        path = '{org_uuid}/tags/application/{app_id}'.format(org_uuid=org_uuid, app_id=app_id)
        return self._delete(path, data={'tag': tag})

    def delete_tag_from_trace(self, org_uuid, trace_id, tag):
        path = '{org_uuid}/tags/trace/{trace_id}'.format(org_uuid=org_uuid, trace_id=trace_id)
        return self._delete(path, data={'tag': tag})

    def delete_tag_from_server(self, org_uuid, server_id, tag):
        path = '{org_uuid}/tags/server/{server_id}'.format(org_uuid=org_uuid, server_id=server_id)
        return self._delete(path, data={'tag': tag})

    def delete_tag_from_library(self, org_uuid, library_hash, tag):
        path = '{org_uuid}/tags/library/{library_hash}'.format(org_uuid=org_uuid, library_hash=library_hash)
        return self._delete(path, data={'tag':tag})