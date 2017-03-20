class ServerLibraryFilter(object):
    QuickFilterAll = 'ALL'
    QuickFilterVulnerable = 'VULNERABLE'
    QuickFilterViolation = 'VIOLATION'
    QuickFilterCustom = 'CUSTOM'
    QuickFilterNonCustom = 'NON_CUSTOM'
    QuickFilterStale = 'STALE'

    ExpandVulns = 'vulns'
    ExpandApps = 'apps'

    def __init__(self):
        self.apps = []
        self.tags = []
        self.expand = []
        self.query = None
        self.quick_filter = ServerLibraryFilter.QuickFilterAll

    def get_params_as_json(self):
        return {
            'apps': ','.join(self.apps),
            'tags': ','.join(self.tags),
            'expand': ','.join(self.expand),
            'q': self.query,
            'quickFilter': self.quick_filter,
        }
