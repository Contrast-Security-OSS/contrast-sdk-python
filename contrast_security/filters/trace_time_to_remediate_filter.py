class TraceTimeToRemediateFilter(object):

    def __init__(self):
        self.apps = []
        self.importance = []
        self.environments = []
        self.servers = []
        self.tags = []
        self.interval = 'WEEK'
        self.expand = []

    def get_params_as_json(self):
        return {
            'apps':  ','.join(self.apps),
            'importance': ','.join(self.importance),
            'environments': ','.join(self.environments),
            'servers': ','.join(self.servers),
            'tags': ','.join(self.tags),
            'expand': ','.join(self.expand),
            'interval': self.interval
        }