import unittest
from color import Color


class TestColor(unittest.TestCase):

    def setUp(self):
        self.color1 = Color(42, 42, 42)
        self.color2 = Color(210, 210, 210)
        self.color3 = Color(42, 21, 58)
        self.color4 = Color(240, 41, 25)

    def tearDown(self):
        pass

    def test_color(self):
        self.assertTrue(self.color1.enough_contrast(self.color2))
        self.assertFalse(self.color3.enough_contrast(self.color4))


if __name__ == "__main__":
    unittest.main()
