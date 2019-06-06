from .api_support import _ApiSupport


class _WebhookApi(_ApiSupport):

    def __init__(self):
        super(_WebhookApi, self).__init__()

    def get_webhooks(self, org_uuid, expand=None):
        path = '{org_uuid}/webhooks'.format(org_uuid=org_uuid)
        return self._get(path, params={'expand': expand})

    def get_webhook(self, org_uuid, webhook_id, expand=None):
        path = '{org_uuid}/webhooks/{webhook_id}'.format(org_uuid=org_uuid, webhook_id=webhook_id)
        return self._get(path, params={'expand': expand})
