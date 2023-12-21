from hw3 import find_pairs_naive, find_pairs_optimized
import unittest

class TestImplementation(unittest.TestCase):

    def test_find_pairs_naive(self):
        '''
        tests correctness of find_pairs__naive func
        '''
        lst = [1, 2, 3, 4, 5]
        lst2 = [0, 1, 2, 3, 4, 5]
        lst3 = [2, 5]
        lst4 = []
        x = find_pairs_naive(lst, 5)
        y = find_pairs_naive(lst, 0)
        z = find_pairs_naive(lst2, 0)
        i = find_pairs_naive(lst3, 4)
        j = find_pairs_naive(lst4, 5)
        self.assertEqual({(2, 3), (1, 4)}, x)
        self.assertEqual(set(), y)
        self.assertEqual(set(), z)
        self.assertEqual(set(), i)
        self.assertEqual(set(), j)

    def test_find_pairs_optimized(self):
        '''
        tests correctness of find_pairs_optimized func
        '''
        lst = [1, 2, 3, 4, 5]
        lst2 = [0, 1, 2, 3, 4, 5]
        lst3 = [2, 5]
        lst4 = []
        x = find_pairs_optimized(lst, 5)
        y = find_pairs_optimized(lst, 0)
        z = find_pairs_optimized(lst2, 0)
        i = find_pairs_optimized(lst3, 4)
        j = find_pairs_optimized(lst4, 5)
        self.assertEqual({(2, 3), (1, 4)}, x)
        self.assertEqual(set(), y)
        self.assertEqual(set(), z)
        self.assertEqual(set(), i)
        self.assertEqual(set(), j)

if __name__ == '__main__':
    unittest.main() # Runs all tests above
