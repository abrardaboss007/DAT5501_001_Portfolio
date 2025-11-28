# Hey Ed, in order to run this test suite as well as all others, please open a new terminal and type pytest

import unittest
from streamlit.testing.v1 import AppTest

class TestCompoundInterestCalculator(unittest.TestCase):
    def test_calculator(self):
        # Bring in file that is being tested
        at = AppTest.from_file("compound_interest_calculator.py").run()

        # Test to see if the two number input tools are working (values should now be 1000.01 and 10.01 respectively)
        at.number_input[0].increment().run()
        at.number_input[1].increment().run()
        
        # Set slider to value of 1
        at.slider[0].set_value(1).run()

        # Test to see if expected outcomes occur
        self.assertEqual(at.markdown[0].value, "Savings after year 1: **1100.11**")
        self.assertEqual(at.markdown[1].value, "It will take **7.27** years to double your money, or approximately **7** years and **98** days")

if __name__ == "__main__":
    unittest.main()
