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
        self.substatus = []
        self.vuln_types = []
        self.app_version_tags = []
        self.servers = []
        self.environments = []
        self.servers = []
        self.urls = []
        self.sinks = []
        self.sinks_values = []
        self.routes = []
        self.modules = []
        self.app_tags = []
        self.app_id = None
        self.quick_filter = "all"
        self.security_standards = []
        self.tracked = False
        self.untracked = False
        self.timestamp_filter = "LAST"
        self.match_route_path_params = False
        self.metadata_filters = []
        self.licensed_only = False
        self.expand = []
        self.limit = 20
        self.offset = 0
        self.sort = '-lastTimeSeen'

    def get_body_params_as_json(self):
        return {
            'filterText': self.filter_text,
            'startDate': self.start_date,
            'endDate': self.end_date,
            'filterTags': ','.join(self.filter_tags),
            'severities': ','.join(self.severities),
            'status': ','.join(self.statuses),
            'substatus': ','.join(self.substatus),
            'vulnTypes': ','.join(self.vuln_types),
            'appVersionTags': ','.join(self.app_version_tags),
            'servers': ','.join(self.servers),
            'environments': ','.join(self.environments),
            'urls': ','.join(self.urls),
            'sinks': ','.join(self.sinks),
            'sinkValues': ','.join(self.sinks_values),
            'routes': ','.join(self.routes),
            'modules': ','.join(self.modules),
            'applicationTags': ','.join(self.app_tags),
            'applicationID': self.app_id,
            'quickFilter': self.quick_filter,
            'securityStandards': ','.join(self.security_standards),
            'tracked': self.tracked,
            'untracked': self.untracked,
            'timestampFilter': self.timestamp_filter,
            'matchRoutePathParams': self.match_route_path_params,
            'metadataFilters': ','.join(self.metadata_filters),
            'licensedOnly': self.licensed_only
        }

    def get_query_params_as_json(self):
        return {
            'expand': ','.join(self.expand),
            'limit': self.limit,
            'offset': self.offset,
            'sort': self.sort
        }
