#!/usr/bin/env python3
"""
data_tests.py has tests for data.py

Brian Ishii 2017
"""


import unittest
import os

from data import *
class DataTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        test = Data("2015-01-02", "2015-01-06")
        cls.test = test
        cls.cwd = os.getcwd()

    def test_path_to_symbol_aapl(self):
        self.assertEqual(self.test.path_to_symbol("AAPL"),
               self.cwd + "/AAPL.csv")

    def test_path_to_symbol_spy(self):
        self.assertEqual(self.test.path_to_symbol("SPY"),
               self.cwd + "/SPY.csv")

    def test_get_data(self):
        output = ("" 
        + "                   SPY\n"
        + "2015-01-02  197.045185\n"
        + "2015-01-05  193.486620\n"
        + "2015-01-06  191.664176\n"
        + "2015-01-07  194.052535\n"
        + "2015-01-08  197.496002\n"
        + "2015-01-09  195.913355\n"
        + "2015-01-12  194.378654\n"
        + "2015-01-13  193.831927")
        temp = Data("2015-01-02", "2015-01-13")
        self.assertEqual(str(temp.get_data()), output)

    def test_get_dates(self):
        dates = ("DatetimeIndex(['2015-01-02',"
        + " '2015-01-03', '2015-01-04', '2015-01-05',\n" 
        + "               '2015-01-06'],\n"
        + "              dtype='datetime64[ns]', freq='D')")
        self.assertEqual(
                str(self.test.get_dates("2015-01-02", "2015-01-06")),
                dates)

    def test_get_bollinger_bands_error(self):
        self.assertRaises(IndexError, self.test.get_bollinger_bands, "AAPL")

    def test_get_bollinger_bands(self):
        temp = Data("2015-01-01", "2015-01-15")
        rm = ("2015-01-02           NaN\n"
        + "2015-01-05           NaN\n"
        + "2015-01-06           NaN\n"
        + "2015-01-07           NaN\n"
        + "2015-01-08    194.748904\n"
        + "2015-01-09    194.522538\n"
        + "2015-01-12    194.700944\n"
        + "2015-01-13    195.134495\n"
        + "2015-01-14    194.856332\n"
        + "2015-01-15    193.536497\n"
        + "Name: SPY, dtype: float64")
        ub =  ("2015-01-02           NaN\n"
        + "2015-01-05           NaN\n"
        + "2015-01-06           NaN\n"
        + "2015-01-07           NaN\n"
        + "2015-01-08    199.689884\n"
        + "2015-01-09    199.021440\n"
        + "2015-01-12    199.063118\n"
        + "2015-01-13    198.236422\n"
        + "2015-01-14    198.621840\n"
        + "2015-01-15    197.302006\n"
        + "Name: SPY, dtype: float64")
        lb =  ("2015-01-02           NaN\n"
        + "2015-01-05           NaN\n"
        + "2015-01-06           NaN\n"
        + "2015-01-07           NaN\n"
        + "2015-01-08    189.807923\n"
        + "2015-01-09    190.023635\n"
        + "2015-01-12    190.338771\n"
        + "2015-01-13    192.032567\n"
        + "2015-01-14    191.090823\n"
        + "2015-01-15    189.770988\n"
        + "Name: SPY, dtype: float64")
        test_rm, test_ub, test_lb = temp.get_bollinger_bands("SPY", window=5)
        self.assertEqual(str(test_rm), rm)
        self.assertEqual(str(test_ub), ub)
        self.assertEqual(str(test_lb), lb)

if __name__ == '__main__':
    unittest.main()
