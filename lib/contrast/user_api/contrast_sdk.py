from util import Util
from forwardable import def_delegator, def_delegators
from applications_api import _ApplicationApi


class ContrastSdk(object):
    def_delegator('_applications', 'get_applications')

    def __init__(self, username, api_key, service_key, teamserver_url='https://app.contrastsecurity.com/Contrast'):
        self._username = username
        self._api_key = api_key
        self._service_key = service_key
        self._teamserver_url = teamserver_url

        self._applications = _ApplicationApi()
        self._configure_api_defaults(self._applications)

        if not Util.validate_url(self._teamserver_url):
            raise ValueError('Invalid Url')

    def _configure_api_defaults(self, api_class):
        api_class._headers = self._create_headers()
        api_class._base_url = self._teamserver_url + '/api'

    def _create_headers(self):
        return {
                    'Authorization': Util.create_authorization_token(self._username, self._service_key),
                    'API-Key': self._api_key
                }

    def _configure_application_api(self):
        self._applications = _ApplicationApi()
        self._configure_api_defaults(self._applications)