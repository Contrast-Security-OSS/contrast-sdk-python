class TraceTrendFilter(object):

    def __init__(self):
        self.rule_severities = []
        self.rules = []
        self.all_rules = None
        self.application_importance = None
        self.application_ids = []
        self.all_applications = None
        self.server_environments = []
        self.servers = []
        self.all_servers = None

    def get_params_as_json(self):
        return {
            'ruleSeverities':  ','.join(self.rule_severities),
            'rules': ','.join(self.rules),
            'allRules': self.all_rules,
            'applicationImportance': self.application_importance,
            'applicationIds': self.application_ids,
            'allApplications': self.all_applications,
            'serverEnvironments': self.server_environments,
            'servers': self.servers,
            'allServers': self.all_servers
        }