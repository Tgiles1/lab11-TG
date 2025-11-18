#https://github.com/Tgiles1/lab11-TG.git
#Partner 1: Tim Giles

import unittest
from calculator import *



class TestCalculator(unittest.TestCase):
    ######### Partner 2
    # def test_add(self): # 3 assertions
    #     fill in code

    # def test_subtract(self): # 3 assertions
    #     fill in code
    # ##########################

    ######## Partner 1
    def test_multiply(self):  
        self.assertEqual(mul(2, 3), 6)  
        self.assertEqual(mul(-4, 5), -20) 
        self.assertEqual(mul(0, 100), 0)      

    def test_divide(self): 
        self.assertEqual(div(2, 10), 5)        
        self.assertEqual(div(4, 1), 0.25) 
        with self.assertRaises(ZeroDivisionError): 
            div(0, 5)

    ######## Partner 2
    # def test_divide_by_zero(self): # 1 assertion
    #     # call division function inside, example:
    #     # with self.assertRaises(<INSERT_ERROR_TYPE>):
    #     #     div(0, 5)
    #     fill in code

    # def test_logarithm(self): # 3 assertions
    #     fill in code

    # def test_log_invalid_base(self): # 1 assertion
    #     # use same technique from test_divide_by_zero
    #     fill in code
    # ##########################
    
    def test_log_invalid_argument(self):
        with self.assertRaises(ValueError):
            logarithm(0, 5)

    def test_hypotenuse(self):
        self.assertEqual(hypotenuse(3, 4), 5)
        self.assertEqual(hypotenuse(0, 0), 0)
        self.assertEqual(hypotenuse(-3, 4), 5)

    def test_sqrt(self):
        with self.assertRaises(ValueError):
            square_root(-1)
        self.assertEqual(square_root(0), 0)
        self.assertEqual(square_root(9), 3)

# Do not touch this
if __name__ == "__main__":
    unittest.main()