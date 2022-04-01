# Write two unittest test cases for the `subtract_divide()` function
# in `mymath.py`
#
# 1. Check for correct results by providing example input.
# 2. Check that a `CustomZeroDivisionError` gets raised correctly.

import unittest
import mymath

class TestMyMath(unittest.TestCase):

    def test_if_generate_correct_result(self):
        self.assertEqual(mymath.subtract_divide(12,6,2), 3)

    def test_check_CustomZeroDivisionError_raised_correctly(self):
        #Ai wonders if there is a way to make line17 work instead of using "with" at the line18.
        # self.assertRaises(mymath.CustomZeroDivsionError,mymath.subtract_divide(4,0,0)) 
        with self.assertRaises(mymath.CustomZeroDivsionError) as context:
            mymath.subtract_divide(4,0,0)
        print(context.exception)

if __name__ == "__main__":
    unittest.main()