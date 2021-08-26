from .api_support import _ApiSupport
import re
from ..types.AgentTypes import AgentTypes


class _AgentApi(_ApiSupport):

    def __init__(self):
        super(_AgentApi, self).__init__()

    def get_agent_profiles(self, org_uuid, expand=None):
        path = '{org_uuid}/agents/profiles'.format(org_uuid=org_uuid)
        return self._get(path, params={'expand': expand})

    def get_agent_profile(self, org_uuid, profile, expand=None):
        path = '{org_uuid}/agents/profiles/{profile}'.format(org_uuid=org_uuid, profile=profile)
        return self._get(path, params={'expand': expand})

    def get_agent_versions(self, org_uuid):
        path = '{org_uuid}/agents/versions'.format(org_uuid=org_uuid)
        return self._get(path)

    def download_agent(self, org_uuid, platform=AgentTypes.JAVA, profile='default', jvm=None):
        path = '{org_uuid}/agents/{profile}/{platform}'.format(org_uuid=org_uuid, profile=profile, platform=platform)
        response = self._download(path, params={'jvm': jvm})
        contrast_name = re.findall("filename=(\S+)", response.headers['content-disposition'])
        with open(contrast_name[0], 'w+') as f:
            for chunk in response.iter_content(chunk_size=1024):
                if chunk:
                    f.write(chunk)
            return response

