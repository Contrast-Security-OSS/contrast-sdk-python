from .api_support import _ApiSupport


class _AgentSessionApi(_ApiSupport):

    def __init__(self):
        super(_AgentSessionApi, self).__init__()

    def filter_app_agent_sessions(self, org_uuid, app_id):
        path = '{orgUuid}/applications/{appId}/agent-sessions'.format(org_uuid=org_uuid, app_id=app_id)
        return self._get(path, json={})

    def filter_app_agent_sessions_filter(self, org_uuid, app_id, limit=None, offset=None):
        path = '{orgUuid}/applications/{appId}/agent-sessions/filter'.format(org_uuid=org_uuid, app_id=app_id)

        # Prepare query parameters
        params = {}
        if limit is not None:
            params['limit'] = limit
        if offset is not None:
            params['offset'] = offset

        return self._post(path, json={}, params=params)

    def filter_app_agent_sessions_latest(self, org_uuid, app_id):
        path = '{orgUuid}/applications/{appId}/agent-sessions/latest'.format(org_uuid=org_uuid, app_id=app_id)
        return self._get(path, json={})

    def filter_app_agent_sessions_sessionid(self, org_uuid, app_id, session_id):
        path = '{orgUuid}/applications/{appId}/agent-sessions/{sessionId}'.format(org_uuid=org_uuid, app_id=app_id, session_id=session_id)
        return self._get(path, json={})


