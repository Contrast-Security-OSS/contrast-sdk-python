class ApplicationTraceFilter(object):
    ExpandCard = 'card'
    ExpandEvents = 'events'
    ExpandNotes = 'notes'
    ExpandRequest = 'request'
    ExpandApplication = 'application'
    ExpandServers = 'servers'

    TimestampFilterFirst = 'FIRST'
    TimestampFilterLast = 'LAST'

    def __init__(self):
        self.filter_text = None
        self.start_date = None
        self.end_date = None
        self.filter_tags = []
        self.severities = []
        self.statuses = []
        self.vuln_types = []
        self.environments = []
        self.servers = []
        self.urls = []
        self.modules = []
        self.timestamp_filter = None
        self.expand = []
        self.limit = 20
        self.offset = 0
        self.sort = '-lastTimeSeen'

    def get_params_as_json(self):
        return {
            'expand': ','.join(self.expand),
            'filterText': self.filter_text,
            'startDate': self.start_date,
            'endDate': self.end_date,
            'servers': ','.join(self.servers),
            'filterTags': ','.join(self.filter_tags),
            'severities': ','.join(self.severities),
            'environments': ','.join(self.environments),
            'status': ','.join(self.statuses),
            'vulnTypes': ','.join(self.vuln_types),
            'modules': self.modules,
            'urls': self.urls,
            'limit': self.limit,
            'offset': self.offset,
            'sort': self.sort
        }