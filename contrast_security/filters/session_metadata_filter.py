class SessionMetadataFilter(object):
    ExpandCard = 'card'
    ExpandEvents = 'events'
    ExpandNotes = 'notes'
    ExpandRequest = 'request'
    ExpandApplication = 'application'
    ExpandServers = 'servers'

    TimestampFilterFirst = 'FIRST'
    TimestampFilterLast = 'LAST'

    """
      ALL("all"),
  OPEN("open"),
  HIGH_CONFIDENCE("high-confidence"),
  VIOLATION("violation"),
  PENDING_REVIEW("pending-review");"""

    def __init__(self):
        self.filter_text = None
        self.start_date = None
        self.end_date = None
        self.filter_tags = []
        self.severities = []
        self.status = []
        self.substatus = []
        self.vuln_types = []
        self.app_version_tags = []
        self.servers = []
        self.environments = []
        self.urls = []
        self.routes = []
        self.modules = []
        self.application_tags = []
        self.application_id = []
        self.quick_filter = []
        self.security_standards = []
        self.tracked = False
        self.untracked = False
        self.timestamp_filter = None
        self.match_route_path_params = False
        self.metadata_filters = []
        self.licensed_only = False

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