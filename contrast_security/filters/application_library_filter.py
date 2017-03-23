class ApplicationLibraryFilter(object):
    QuickFilterAll = 'ALL'
    QuickFilterVulnerable = 'VULNERABLE'
    QuickFilterViolation = 'VIOLATION'
    QuickFilterCustom = 'CUSTOM'
    QuickFilterNonCustom = 'NON_CUSTOM'
    QuickFilterStale = 'STALE'

    ExpandVulns = 'vulns'
    ExpandApps = 'apps'
    ExpandQuickFilters = 'quickFilters'

    def __init__(self):
        self.servers = []
        self.tags = []
        self.expand = []
        self.query = None
        self.quick_filter = ApplicationLibraryFilter.QuickFilterAll

    def get_params_as_json(self):
        return {
            'servers': ','.join(self.servers),
            'tags': ','.join(self.tags),
            'expand': ','.join(self.expand),
            'q': self.query,
            'quickFilter': self.quick_filter,
        }