import unittest
from knapsack import bruteKnapsack, bruteFracKnapsack, greedyKnapsack, dynamicKnapsack


class KnapsackTest(unittest.TestCase):
    def test_brute(self):
        w = [10, 20, 30, 40]
        p = [20, 30, 60, 40]
        self.assertEqual(bruteKnapsack(w, p, 60), 110)

    def test_bruteFrac(self):
        w = [10, 20, 30, 40]
        p = [20, 30, 60, 40]
        self.assertEqual(bruteFracKnapsack(w, p, 55), 102.5)

    def test_greedy(self):
        w = [15, 25, 45, 60, 75, 90]
        p = [2, 8, 7, 11, 22, 30]
        self.assertEqual(greedyKnapsack(w, p, 150), 48.266666666666666)

    def test_dynamic(self):
        w = [10, 20, 30, 40, 50, 60, 70, 80, 90]
        p = [12, 18, 15, 25, 21, 27, 30, 22, 29]
        self.assertEqual(dynamicKnapsack(w, p, 150), 91)


if __name__ == '__main__':
    unittest.main()
