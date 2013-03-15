import unittest
from restaurant import Restaurant


class TestRestaurant(unittest.TestCase):

    def setUp(self):
        self.restaurant = Restaurant(
            {"rice" : 3, "noodles" : 2})

    def tearDown(self):
        pass

    def test_restaurant(self):
        self.assertEqual(0, self.restaurant.cost())
        self.assertEqual(15, self.restaurant.cost(
                {"rice" : 1, "noodles" : 1},
                {"rice" : 2, "noodles" : 2}))


if __name__ == "__main__":
    unittest.main()
