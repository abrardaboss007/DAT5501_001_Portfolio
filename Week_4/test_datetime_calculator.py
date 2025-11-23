import unittest
from streamlit.testing.v1 import AppTest
import datetime


at = AppTest.from_file("datetime_calculator.py").run()


todays_date= datetime.date.today()
yesterdays_date = todays_date - datetime.timedelta(days=1)
tomorrows_date = todays_date + datetime.timedelta(days=1)

class TestDatetimeCalculator(unittest.TestCase):
    def test_user_input_initial_task(self):

        #assert min_value max_value label
        assert at.date_input[0].value == None

        assert at.date_input[0].label == "Enter a date in the past"
        assert at.date_input[0].min == datetime.date(1970,1,1)
        assert at.date_input[0].max == yesterdays_date

        assert at.date_input[1].value == None

        assert at.date_input[1].label == "Enter a date in the future"
        assert at.date_input[1].min == tomorrows_date
        assert at.date_input[1].max == datetime.date(2070,1,1)

        past_date =  datetime.date(1999,7,20)
        future_date = datetime.date(2030,12,31)

        at.date_input[0].set_value(past_date).run()
        at.date_input[1].set_value(future_date).run()

        assert at.date_input[0].value == past_date
        assert at.date_input[1].value == future_date



if __name__ == "__main__":
    unittest.main()

