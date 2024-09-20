from .api_support import _ApiSupport


class _SessionMetadataApi(_ApiSupport):

    def __init__(self):
        super(_SessionMetadataApi, self).__init__()

    def filter_app_session_metadata(self, org_uuid, app_id):
        path = '{org_uuid}/metadata/session/{app_id}/filters'.format(org_uuid=org_uuid, app_id=app_id)
        return self._post(path, json={})

    def get_app_agentsessions(self, org_uuid, app_id):
        path = '{org_uuid}/applications/{appId}/agent-sessions'.format(org_uuid=org_uuid, app_id=app_id)
        return self._get(path)

    def filter_app_session_metadata_filter(self, org_uuid, app_id, limit=None, offset=None):
        path = '{org_uuid}/applications/{appId}/agent-sessions/filter'.format(org_uuid=org_uuid, app_id=app_id)

        # Prepare query parameters
        params = {}
        if limit is not None:
            params['limit'] = limit
        if offset is not None:
            params['offset'] = offset

        return self._post(path, params=params)

    def get_app_session_metadata_latest(self, org_uuid, app_id):
        path = '{org_uuid}/applications/{appId}/agent-sessions/latest'.format(org_uuid=org_uuid, app_id=app_id)
        return self._get(path)

    def get_app_session_metadata_sessionid(self, org_uuid, app_id, session_id):
        path = '{org_uuid}/applications/{appId}/agent-sessions/{sessionId}'.format(org_uuid=org_uuid, app_id=app_id, session_id=session_id)
        return self._get(path)
