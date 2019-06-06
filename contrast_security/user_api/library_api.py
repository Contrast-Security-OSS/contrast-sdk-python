from .api_support import _ApiSupport
from ..filters.library_filter import LibraryFilter

class _LibraryApi(_ApiSupport):

    def __init__(self):
        super(_LibraryApi, self).__init__()

    def get_libraries(self, org_uuid, expand=None, quick_filter='ALL'):
        path = '{org_uuid}/libraries'.format(org_uuid=org_uuid)
        return self._get(path, params={'expand': expand, 'quickFilter': quick_filter})

    def get_dotnet_library(self, org_uuid, library_hash, expand=None):
        path = '{org_uuid}/libraries/dotnet/{library_hash}'.format(org_uuid=org_uuid, library_hash=library_hash)
        return self._get(path, params={'expand': expand})

    def get_java_library(self, org_uuid, library_hash, expand=None):
        path = '{org_uuid}/libraries/java/{library_hash}'.format(org_uuid=org_uuid, library_hash=library_hash)
        return self._get(path, params={'expand': expand})

    def get_library_stats(self, org_uuid):
        path = '{org_uuid}/libraries/stats'.format(org_uuid=org_uuid)
        return self._get(path)

    def get_library_filter_subfilters(self, org_uuid,filter_type):
        path = '{org_uuid}/libraries/filters/{filter_type}/listing'.format(org_uuid=org_uuid, filter_type=filter_type)
        return self._get(path)

    def filter_libraries(self, org_uuid, library_filter=None):
        if library_filter is None:
            library_filter = LibraryFilter()
        path = '{org_uuid}/libraries/filter'.format(org_uuid=org_uuid)
        return self._get(path, params=library_filter.get_params_as_json())

    def get_all_library_filters(self, filter_type):
        return self._get('libraries/filters/listing', params={'filterType': filter_type})

    def get_library_policy(self, org_uuid):
        path = '{org_uuid}/library/policy'.format(org_uuid=org_uuid)
        return self._get(path)

