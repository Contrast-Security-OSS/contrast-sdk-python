import contrast_security.filters.filter_utils as utils


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
        self.quick_filter = "ALL"
        self.metadata_filters = []
        self.expand = []
        self.include_merged = False
        self.limit = 20
        self.offset = 0
        self.sort = '-appName'

    def get_body_params_as_json(self):
        return {
            'filterText': utils.parse_single_element_list_to_string(self.filter_text),
            'filterAppCode': self.filter_appcode,
            'filterServers': self.filter_servers,
            'filterTechs': self.filter_techs,
            'filterTags': self.filter_tags,
            'filterLanguages': self.filter_languages,
            'filterCompliance': self.filter_compliance,
            'environment': self.environment,
            'appImportances': self.app_importances,
            'filterVulnSeverities': self.filter_vulnerabilities_severities,
            'includeArchived': self.include_archived,
            'includeOnlyLicensed': self.include_only_license,
            'quickFilter': self.quick_filter,
            'metadataFilters': self.metadata_filters
        }

    def get_query_params_as_json(self):
        return {
            'expand': ','.join(self.expand),
            'includeMerged': self.include_merged,
            'limit': self.limit,
            'offset': self.offset,
            'sort': self.sort
        }
