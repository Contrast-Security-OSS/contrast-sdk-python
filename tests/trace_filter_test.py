from unittest import TestCase

from contrast_security.filters.trace_filter import TraceFilter

class TraceFilterTest(TestCase):

    @classmethod
    def setUpClass(cls):
        super(TraceFilterTest, cls).setUpClass()

    def trace_quick_filter_enum_open_test(self):
        self.assertEqual('OPEN', TraceFilter.VulnerabilityQuickFilter_Open)

    def trace_quick_filter_enum_high_confidence_test(self):
        self.assertEqual('HIGH_CONFIDENCE', TraceFilter.VulnerabilityQuickFilter_HighConfidence)