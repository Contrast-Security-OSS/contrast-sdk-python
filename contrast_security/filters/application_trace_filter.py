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
        self.quick_filter = "ALL"
        self.security_standards = []
        self.tracked = True
        self.untracked = True
        self.timestamp_filter = None
        self.match_route_path_params = True
        self.metadata_filters = []
        self.licensed_only = True
        self.expand = []
        self.limit = 20
        self.offset = 0
        self.sort = '-lastTimeSeen'

    def get_body_params_as_json(self):
        return {
            'appVersionTags': self.app_version_tags,
            'applicationID': self.app_id,
            'applicationTags': self.app_tags,
            'startDate': self.start_date,
            'endDate': self.end_date,
            'environments': self.environments,
            'filterTags': self.filter_tags,
            'filterText': self.filter_text,
            'licensedOnly': self.licensed_only,
            'matchRoutePathParams': self.match_route_path_params,
            'metadataFilters': self.metadata_filters,
            'modules': self.modules,
            'quickFilter': self.quick_filter,
            'routes': self.routes,
            'securityStandards': self.security_standards,
            'servers': self.servers,
            'severities': self.severities,
            'sinks': self.sinks,
            'sinkValues': self.sinks_values,
            'status': self.statuses,
            'substatus': self.substatus,
            'timestampFilter': self.timestamp_filter,
            'tracked': self.tracked,
            'untracked': self.untracked,
            'urls': self.urls,
            'vulnTypes': self.vuln_types,
        }

    def get_query_params_as_json(self):
        return {
            'expand': ','.join(self.expand),
            'limit': self.limit,
            'offset': self.offset,
            'sort': self.sort
        }
