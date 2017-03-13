class ServerFilter(object):
    QuickFilterAll = 'ALL'
    QuickFilterAccessEnabled = 'ACCESS_ENABLED'
    QuickFilterProtectEnabled = 'PROTECT_ENABLED'
    QuickFilterOutOfDate = 'OUT_OF_DATE'

    ExpandApplications = 'applications'
    ExpandNumberApps = 'num_apps'

    def __init__(self):
        self.application_ids = []
        self.log_levels = []
        self.tags = []
        self.agent_versions = []
        self.environments = []
        self.expand = []
        self.include_archived = False
        self.query = None
        self.quick_filter = ServerFilter.QuickFilterAll
        self.limit = 20
        self.offset = 0
        self.sort = 'lastActivity'

    def get_params_as_json(self):
        return {
            'applicationIds': ','.join(self.application_ids),
            'logLevels': ','.join(self.log_levels),
            'tags': ','.join(self.tags),
            'agentVersions': ','.join(self.agent_versions),
            'environments': ','.join(self.environments),
            'expand': ','.join(self.expand),
            'includeArchived': self.include_archived,
            'query': self.query,
            'quickFilter': self.quick_filter,
            'limit': self.limit,
            'offset': self.offset,
            'sort': self.sort
        }
