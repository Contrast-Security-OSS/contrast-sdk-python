from .api_support import _ApiSupport


class _ScoresApi(_ApiSupport):

    def __init__(self):
        super(_ScoresApi, self).__init__()

    def get_overall_scores(self, org_uuid):
        path = '{org_uuid}/scores'.format(org_uuid=org_uuid)
        return self._get(path)

    def get_score_category_breakdown(self, org_uuid):
        path = '{org_uuid}/scores/breakdown/category'.format(org_uuid=org_uuid)
        return self._get(path)

    def get_score_rule_breakdown(self, org_uuid):
        path = '{org_uuid}/scores/breakdown/rule'.format(org_uuid=org_uuid)
        return self._get(path)

    def get_score_server_breakdown(self, org_uuid):
        path = '{org_uuid}/scores/breakdown/server'.format(org_uuid=org_uuid)
        return self._get(path)

    def get_score_severity_breakdown(self, org_uuid):
        path = '{org_uuid}/scores/breakdown/severity'.format(org_uuid=org_uuid)
        return self._get(path)

    def get_score_status_breakdown(self, org_uuid):
        path = '{org_uuid}/scores/breakdown/status'.format(org_uuid=org_uuid)
        return self._get(path)

    def get_score_trace_rule_breakdown(self, org_uuid):
        path = '{org_uuid}/scores/breakdown/trace/rule'.format(org_uuid=org_uuid)
        return self._get(path)

    def get_score_trace_severity_breakdown(self, org_uuid):
        path = '{org_uuid}/scores/breakdown/trace/severity'.format(org_uuid=org_uuid)
        return self._get(path)

    def get_score_trace_status_breakdown(self, org_uuid):
        path = '{org_uuid}/scores/breakdown/trace/status'.format(org_uuid=org_uuid)
        return self._get(path)

    def get_score_platform(self, org_uuid):
        path = '{org_uuid}/scores/platform'.format(org_uuid=org_uuid)
        return self._get(path)

    def get_score_platform_include_defense(self, org_uuid):
        path = '{org_uuid}/scores/platform/defense'.format(org_uuid=org_uuid)
        return self._get(path)

    def get_score_security(self, org_uuid):
        path = '{org_uuid}/scores/security'.format(org_uuid=org_uuid)
        return self._get(path)

    def get_score_security_include_defense(self, org_uuid):
        path = '{org_uuid}/scores/security/defense'.format(org_uuid=org_uuid)
        return self._get(path)