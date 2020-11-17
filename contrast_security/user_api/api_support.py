import requests


class _ApiSupport(object):
    _headers = None
    _base_url = None

    def __init__(self, version='ng'):
        self._version = version

    def build_url(self, path):
        return '{base_url}/{version}/{path}'.format(base_url=self._base_url,  version=self._version, path=path)

    def _get(self, path, params=None):
        return requests.get(self.build_url(path), params=params, headers=self._headers)

    def _post(self, path, data=None, params=None):
        return requests.post(self.build_url(path), json=data, headers=self._headers, params=params)

    def _put(self, path, data=None):
        return requests.put(self.build_url(path), json=data, headers=self._headers)

    def _download(self, path, params=None):
        return requests.get(self.build_url(path), params=params, headers=self._headers, stream=True)

    def _delete(self, path, data=None):
        return requests.delete(self.build_url(path), json=data, headers=self._headers)

