import unittest
import Coins


class TestCoins(unittest.TestCase):
    """ Unit test for Coins module """

    def test_coin_combinations(self):
        self.assertEqual(73682, Coins.coin_combinations([200, 100, 50, 20, 10, 5, 2, 1], 0, 7, 200))
        self.assertEqual(3, Coins.coin_combinations([2, 2, 6, 8], 0, 3, 4))
        self.assertEqual(0, Coins.coin_combinations([5, 7, 6, 8], 0, 3, 4))


if __name__ == '__main__':
    unittest.main()
