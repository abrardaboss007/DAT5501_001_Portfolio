import unittest
from streamlit.testing.v1 import AppTest

class TestElectionResults(unittest.TestCase):
    def test_election_data(self):
        at = AppTest.from_file("election_data.py").run()

        # Test to see if toggle has the correct information
        assert at.toggle[0].value == False
        assert at.toggle[0].label == "Compare the vote fraction for two candidates"
        
        # Set toggle to True in order to see if both selectboxes function as intended
        at.toggle[0].set_value(True).run()

        assert at.selectbox[0].value == "John Kasich"
        assert at.selectbox[0].label == "Select first candidate"
        assert at.selectbox[0].options == ["John Kasich", "Ted Cruz", "Ben Carson", "Donald Trump", "Marco Rubio", "Hillary Clinton", "Bernie Sanders", "Martin O'Malley", "Uncommitted", "Carly Fiorina", "Chris Christie", "Mike Huckabee", "Rick Santorum", "Jeb Bush", "Rand Paul", "No Preference"]

        assert at.selectbox[1].value == "Ted Cruz"
        assert at.selectbox[1].label == "Select second candidate"
        assert at.selectbox[1].options == ["Ted Cruz", "Ben Carson", "Donald Trump", "Marco Rubio", "Hillary Clinton", "Bernie Sanders", "Martin O'Malley", "Uncommitted", "Carly Fiorina", "Chris Christie", "Mike Huckabee", "Rick Santorum", "Jeb Bush", "Rand Paul", "No Preference"]

if __name__ == "__main__":
    unittest.main()