import unittest
from candidate import Candidate


class TestCandidate(unittest.TestCase):

    def setUp(self):
        self.enough_year = Candidate(
            2, 499, ["Ruby", "Python"], False, 15)
        self.enough_github = Candidate(
            1, 500, ["Ruby", "Python"], False, 15)
        self.no_year_github = Candidate(
            1, 499, ["Ruby", "Python"], False, 15)
        self.no_python = Candidate(
            2, 499, ["Ruby"], False, 15)
        self.applied = Candidate(
            1, 500, ["Python"], True, 15)
        self.no_age = Candidate(
            2, 499, ["Python"], False, 14)

    def tearDown(self):
        pass

    def test_candidate(self):
        self.assertTrue(self.enough_year.experienced_programmer())
        self.assertTrue(self.enough_github.experienced_programmer())
        self.assertFalse(self.no_year_github.experienced_programmer())
        self.assertFalse(self.no_python.experienced_programmer())
        self.assertFalse(self.applied.experienced_programmer())
        self.assertFalse(self.no_age.experienced_programmer())


if __name__ == "__main__":
    unittest.main()
