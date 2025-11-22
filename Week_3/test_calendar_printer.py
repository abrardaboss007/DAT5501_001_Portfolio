import unittest
from streamlit.testing.v1 import AppTest

at = AppTest.from_file("calendar_printer.py").run()

class TestCalendarPrinter(unittest.TestCase):
    def test_calendar_start_day(self):
        assert at.selectbox[0].options == ["Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"]
        assert at.selectbox[0].label == "**Starting day of the month**"
        assert at.selectbox[0].placeholder == "Select an option..."

        at.selectbox[0].select("Friday").run()
        assert at.selectbox[0].value == "Friday"

        at.selectbox[0].select("Monday").run()
        assert at.selectbox[0].value == "Monday"

        at.selectbox[0].select("Thursday").run()
        assert at.selectbox[0].value == "Thursday"

        at.selectbox[0].select("Sunday").run()
        assert at.selectbox[0].value == "Sunday"

        at.selectbox[0].select("Tuesday").run()
        assert at.selectbox[0].value == "Tuesday"

        at.selectbox[0].select("Wednesday").run()
        assert at.selectbox[0].value == "Wednesday"

        at.selectbox[0].select("Saturday").run()
        assert at.selectbox[0].value == "Saturday"

    def test_calendar_no_day_in_month(self):
        assert at.slider[0].options == []
        assert at.slider[0].label == "**Number of days in the month**"
        
        # Check that the default value is 28
        assert at.slider[0].value == 28

        at.slider[0].set_value(29).run()
        assert at.slider[0].value == 29

        at.slider[0].set_value(30).run()
        assert at.slider[0].value == 30

        at.slider[0].set_value(31).run()
        assert at.slider[0].value == 31

if __name__ == "__main__":
    unittest.main()
