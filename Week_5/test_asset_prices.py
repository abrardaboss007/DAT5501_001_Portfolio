import unittest
from streamlit.testing.v1 import AppTest

class TestCompoundInterestCalculator(unittest.TestCase):
    def test_calculator(self):
        # Use assertions to check if the widget behaves as expected
        at = AppTest.from_file("asset_prices.py").run()

        assert at.text_input[0].value == None
        assert at.text_input[0].label == "Enter the **ticker symbol** of a **US** stock"
        assert at.text_input[0].placeholder == "e.g. AAPL"
        assert at.text_input[0].max_chars == 5

        at.text_input[0].input("NVDA").run()
        assert at.text_input[0].value == "NVDA"

        at.text_input[0].input("HIMS").run()
        assert at.text_input[0].value == "HIMS"

        at.text_input[0].input("QBTS").run()
        assert at.text_input[0].value == "QBTS"

if __name__ == "__main__":
    unittest.main()