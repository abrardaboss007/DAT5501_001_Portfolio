# Hey Ed, in order to run this test suite as well as all others, please open a new terminal and type pytest

import unittest
from streamlit.testing.v1 import AppTest
import datetime

at = AppTest.from_file("datetime_calculator.py").run()

todays_date= datetime.date.today()
yesterdays_date = todays_date - datetime.timedelta(days=1)
tomorrows_date = todays_date + datetime.timedelta(days=1)

class TestDatetimeCalculator(unittest.TestCase):
    def test_user_input_initial_task(self):
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


        def test_extension_activity(self):
            self.assertEqual(at.markdown[0].value, "**Extension Activity**")
            self.assertEqual(at.markdown[1].value, f"There are **{(todays_date - datetime.date(2005,2,15)).days}** days between today and 15/02/2005")
            self.assertEqual(at.markdown[2].value, f"There are **{(todays_date - datetime.date(1993,8,27)).days}** days between today and 27/08/1993")
            self.assertEqual(at.markdown[3].value, f"There are **{(todays_date - datetime.date(2015,8,15)).days}** days between today and 15/08/2015")
            self.assertEqual(at.markdown[4].value, f"There are **{(todays_date - datetime.date(2012,4,13)).days}** days between today and 13/04/2012")
            self.assertEqual(at.markdown[5].value, f"There are **{(todays_date - datetime.date(1993,11,19)).days}** days between today and 19/11/1993")
            self.assertEqual(at.markdown[6].value, f"There are **{(todays_date - datetime.date(2007,12,29)).days}** days between today and 29/12/2007")
            self.assertEqual(at.markdown[7].value, f"There are **{(todays_date - datetime.date(1999,8,2)).days}** days between today and 02/08/1999")
            self.assertEqual(at.markdown[8].value, f"There are **{(todays_date - datetime.date(2017,6,7)).days}** days between today and 07/06/2017")
            self.assertEqual(at.markdown[9].value, f"There are **{(todays_date - datetime.date(1997,3,15)).days}** days between today and 15/03/1997")
            self.assertEqual(at.markdown[10].value, f"There are **{(todays_date - datetime.date(2024,11,24)).days}** days between today and 24/11/2024")
            self.assertEqual(at.markdown[11].value, f"There are **{(todays_date - datetime.date(2011,7,10)).days}** days between today and 10/07/2011")
            self.assertEqual(at.markdown[12].value, f"There are **{(todays_date - datetime.date(1997,12,11)).days}** days between today and 11/12/1997")
            self.assertEqual(at.markdown[13].value, f"There are **{(todays_date - datetime.date(1993,11,17)).days}** days between today and 17/11/1993")
            self.assertEqual(at.markdown[14].value, f"There are **{(todays_date - datetime.date(2001,10,19)).days}** days between today and 19/10/2001")
            self.assertEqual(at.markdown[15].value, f"There are **{(todays_date - datetime.date(2011,10,12)).days}** days between today and 12/10/2011")
            self.assertEqual(at.markdown[16].value, f"There are **{(todays_date - datetime.date(2002,3,1)).days}** days between today and 01/03/2002")
            self.assertEqual(at.markdown[17].value, f"There are **{(todays_date - datetime.date(2015,1,6)).days}** days between today and 06/01/2015")
            self.assertEqual(at.markdown[18].value, f"There are **{(todays_date - datetime.date(2023,5,8)).days}** days between today and 08/05/2023")
            self.assertEqual(at.markdown[19].value, f"There are **{(todays_date - datetime.date(2020,2,16)).days}** days between today and 16/02/2020")


if __name__ == "__main__":
    unittest.main()

