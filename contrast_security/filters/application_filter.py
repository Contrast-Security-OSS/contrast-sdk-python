class ApplicationFilter(object):
    ExpandScores = 'scores'
    ExpandTraceBreakdown = 'trace_breakdown'
    ExpandLicense = 'license'
    ExpandTechnologies = 'technologies'

    def __init__(self):
        self.expand = []
        self.filter_text = None
        self.filter_servers = []
        self.filter_techs = []
        self.filter_tags = []
        self.filter_languages = []
        self.include_archived = False
        self.include_merged = True
        self.limit = 20
        self.offset = 0
        self.sort = '-appName'


    def get_params_as_json(self):
        return {
            'expand': ','.join(self.expand),
            'filterText': self.filter_text,
            'filterServers': ','.join(self.filter_servers),
            'filterTechs': ','.join(self.filter_techs),
            'filterTags': ','.join(self.filter_tags),
            'filterLanguages': ','.join(self.filter_languages),
            'includeArchived': self.include_archived,
            'includeMerged': self.include_merged,
            'limit': self.limit,
            'offset': self.offset,
            'sort': self.sort
        }