import unittest
import snake as s

class snakeTest(unittest.TestCase):

    # Tests for numberOfAvailableDifferentPaths
    def testAcceptanceTests(self):
        self.assertEqual(s.numberOfAvailableDifferentPaths([4, 3], [[2,2], [3,2], [3,1], [3,0], [2,0], [1,0], [0,0]], 3), 7)
        self.assertEqual(s.numberOfAvailableDifferentPaths([2, 3], [[0,2], [0,1], [0,0], [1,0], [1,1], [1,2]], 10), 1)
        self.assertEqual(s.numberOfAvailableDifferentPaths([10, 10], [[5,5], [5,4], [4,4], [4,5]], 4), 81)

    # Tests for selfIntersects
    def test_selfIntersects(self):
        self.assertTrue(s.selfIntersects([[1,1],[2,1],[2,0],[1,0],[0,0]], [1,0]))
        self.assertTrue(s.selfIntersects([[1,1],[2,1],[2,0],[1,0],[0,0]], [2,1]))
        self.assertFalse(s.selfIntersects([[1,1],[2,1],[2,0],[1,0],[0,0]], [0,1]))
        self.assertFalse(s.selfIntersects([[1,1],[2,1],[2,0],[1,0],[0,0]], [1,2]))
        self.assertFalse(s.selfIntersects([[1,1],[2,1],[2,0],[1,0]], [1,0]))

    # Tests for tryLeft
    # Tests for tryUp
    # Tests for tryRight
    # Tests for tryDown