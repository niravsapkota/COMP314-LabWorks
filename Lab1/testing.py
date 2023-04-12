import unittest
from search import linearSearch, binarySearch

class SearchTestCase(unittest.TestCase):
    def test_linear_search(self):
        values = [5, 3, 6, 1, 4, 9, 8]
        self.assertEqual(linearSearch(values, 3),1)
        self.assertEqual(linearSearch(values, 5),0)
        self.assertEqual(linearSearch(values, 1),3)

    def test_binarySearch(self):
        values = [1, 2, 4, 5, 6, 7, 8, 9]
        n=len(values)
        self.assertEqual(binarySearch(values, 0, n, 2),1)
        self.assertEqual(binarySearch(values, 0, n, 8),6)
        self.assertEqual(binarySearch(values, 0, n, 3),-1)

if __name__=='__main__':
    unittest.main()