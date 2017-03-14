class LibraryFilter(object):
    QuickFilterAll = 'ALL'
    QuickFilterVulnerable = 'VULNERABLE'
    QuickFilterViolation = 'VIOLATION'
    QuickFilterCustom = 'CUSTOM'
    QuickFilterNonCustom = 'NONCUSTOM'
    QuickFilterStale = 'STALE'

    ExpandApplications = 'apps'
    ExpandVulns = 'vulns'

    def __init__(self):
        self.apps = []
        self.servers = []
        self.tags = []
        self.query = None
        self.quick_filter = LibraryFilter.QuickFilterAll
        self.expand = []

    def get_params_as_json(self):
        return {
            'apps': ','.join(self.apps),
            'servers': ','.join(self.servers),
            'tags': ','.join(self.tags),
            'q': self.query,
            'quickFilter': self.quick_filter,
            'expand': ','.join(self.expand)
        }
