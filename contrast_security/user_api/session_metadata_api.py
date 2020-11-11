from .api_support import _ApiSupport


class _SessionMetadataApi(_ApiSupport):

    def __init__(self):
        super(_SessionMetadataApi, self).__init__()

    def filter_app_session_metadata(self, org_uuid, app_id):
        path = '{org_uuid}/metadata/session/{app_id}/filters'.format(org_uuid=org_uuid, app_id=app_id)
        return self._get(path)
