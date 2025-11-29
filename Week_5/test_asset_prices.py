import unittest
from streamlit.testing.v1 import AppTest

class TestAssetPrices(unittest.TestCase):
    def test_asset_prices(self):
        # Use assertions to check if the widget behaves as expected
        at = AppTest.from_file("asset_prices.py").run()

        # Test to see if text_input has the correct information
        assert at.text_input[0].label == "Enter the **ticker symbol** of a **US** stock"
        assert at.text_input[0].value == None
        assert at.text_input[0].placeholder == "e.g. AAPL"
        assert at.text_input[0].max_chars== 5

if __name__ == "__main__":
    unittest.main()