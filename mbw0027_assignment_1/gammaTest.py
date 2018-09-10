import unittest
from Warmup.gamma import gamma
import math

class gammaTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.systemUnderTest = __name__

    def setUp(self):
        pass

    def tearDown(self):
        pass

    # 100 gamma
    #    Analysis
    #        inputs:
    #            n:    integer .GE. 1; mandatory; not validated
    #        outputs:
    #            returns:  float
    #    Happy path:
    #        test_010:    nominal value
    #        test_020:    ???
    #
    #    Sad path:
    #        test_910:    alpha n
    #        test_920:    ???
    #
    #+++++++++++ Happy Path Tests ++++++++++++
    #-----------
    def test100_010_ShouldCalculateProbwithMiddleNominal(self):
        self.assertEqual(gamma(10.0), 24.0)

    def test100_020_ShouldCalculateProbwithLowNominal(self):
        self.assertEqual(gamma(1.0), math.sqrt(math.pi))

    def test100_030_ShouldCalculateProbwithNominal2(self):
        self.assertEqual(gamma(2.0), 1.0)

    def test100_040_ShouldCalculateProbwithHighNominal(self):
        self.assertEqual(gamma(12.0), 120.0)

    def test100_040_ShouldCalculateProbwithHighNominal(self):
        self.assertEqual(gamma(5), 120.0)
    #+++++++++++ Sad Path Tests ++++++++++++

    def test100_910_ShouldProduceErrorOnMissingN(self):
        self.assertEqual(gamma(None), 0)
    def test100_920_ShouldProduceErrorOnNonInteger(self):
        self.assertEqual(gamma("a"), 0)
    def test100_920_ShouldProduceErrorOnNEqual0(self):
        self.assertEqual(gamma("0"), 0)
