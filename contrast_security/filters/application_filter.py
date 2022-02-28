class ApplicationFilter(object):
    ExpandScores = 'scores'
    ExpandTraceBreakdown = 'trace_breakdown'
    ExpandLicense = 'license'
    ExpandTechnologies = 'technologies'

    def __init__(self):
        self.filter_text = None
        self.filter_appcode = None
        self.filter_servers = []
        self.filter_techs = []
        self.filter_tags = []
        self.filter_languages = []
        self.filter_compliance = []
        self.environment = []
        self.app_importances = []
        self.filter_vulnerabilities_severities = []
        self.include_archived = False
        self.include_only_license = False
        self.quick_filter = "all"
        self.metadata_filters = []
        self.expand = []
        self.include_merged = False
        self.limit = 20
        self.offset = 0
        self.sort = '-appName'

    def get_body_params_as_json(self):
        return {
            'filterText': self.filter_text,
            'filterAppCode': self.filter_appcode,
            'filterServers': ','.join(self.filter_servers),
            'filterTechs': ','.join(self.filter_techs),
            'filterTags': ','.join(self.filter_tags),
            'filterLanguages': ','.join(self.filter_languages),
            'filterCompliance': ','.join(self.filter_compliance),
            'environment': ','.join(self.environment),
            'appImportances': ','.join(self.app_importances),
            'filterVulnSeverities': ','.join(self.filter_vulnerabilities_severities),
            'includeArchived': self.include_archived,
            'includeOnlyLicensed': self.include_only_license,
            'quickFilter': self.quick_filter,
            'metadataFilters': ','.join(self.metadata_filters)
        }

    def get_query_params_as_json(self):
        return {
            'expand': ','.join(self.expand),
            'includeMerged': self.include_merged,
            'limit': self.limit,
            'offset': self.offset,
            'sort': self.sort
        }
