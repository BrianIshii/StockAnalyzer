import unittest
from trade import *

class TimerTests (unittest.TestCase):
    def test_symbol_to_path_1(self):
        self.assertEqual(symbol_to_path("AAPL"),"StockData/AAPL.csv")
    
    def test_symbol_to_path_2(self):
        self.assertEqual(symbol_to_path("GOOGL"),"StockData/GOOGL.csv")
if __name__ == '__main__':
    unittest.main()