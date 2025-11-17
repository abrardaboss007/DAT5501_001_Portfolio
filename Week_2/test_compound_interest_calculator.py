import unittest
from streamlit.testing.v1 import AppTest

class TestCompoundInterestCalculator(unittest.TestCase):
    def test_calculator(self):
        at = AppTest.from_file("compound_interest_calculator.py").run()

        at.number_input[0].increment().run()
        at.number_input[1].increment().run()
        at.slider[0].set_value(1).run()

        self.assertEqual(at.markdown[0].value, "Savings after year 1: **1100.11**")
        self.assertEqual(at.markdown[1].value, "It will take **7.27** years to double your money")

if __name__ == "__main__":
    unittest.main()
