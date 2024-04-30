from main import Solution
import unittest # Importamos la libreria unittest


class TestSolution(unittest.TestCase):
    def test_twoSum(self):
        self.assertEqual(Solution().twoSum([2, 7, 11, 15], 9), [0, 1])
        self.assertEqual(Solution().twoSum([3, 2, 4], 6), [1, 2])
        self.assertEqual(Solution().twoSum([3, 3], 6), [0, 1])
        self.assertEqual(Solution().twoSum([-1, -2, -3, -4, -5], -8), [2, 4])

    # def sumar(self):
    #     self.assertEqual(Solution().twoSum([2, 7, 11, 15], 9), [0, 0])

if __name__ == '__main__':
    unittest.main()