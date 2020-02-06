from .api_support import _ApiSupport


class _PolicyApi(_ApiSupport):

    def __init__(self):
        super(_PolicyApi, self).__init__()

    def get_validators_and_sanitizers(self, org_uuid):
        path = '{org_uuid}/controls'.format(org_uuid=org_uuid)
        return self._get(path)

    def get_validator_controls(self, org_uuid):
        path = '{org_uuid}/controls/validators'.format(org_uuid=org_uuid)
        return self._get(path)

    def get_sanitizer_controls(self, org_uuid):
        path = '{org_uuid}/controls/sanitizers'.format(org_uuid=org_uuid)
        return self._get(path)

    def get_control_suggestions(self, org_uuid):
        path = '{org_uuid}/controls/suggestion'.format(org_uuid=org_uuid)
        return self._get(path)

