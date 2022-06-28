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
    def test_tryLeft(self):
        self.assertTrue(s.tryLeft([[0,1],[0,2],[0,3]]));
        self.assertTrue(s.tryLeft([[0,1],[1,1],[1,2]]));
        self.assertTrue(s.tryLeft([[0,1],[1,1],[1,0],[0,0]]));
        self.assertFalse(s.tryLeft([[1,1],[2,1],[2,0],[1,0],[0,0]]));
        self.assertFalse(s.tryLeft([[0,0],[1,0],[2,0]]));
        self.assertFalse(s.tryLeft([[1,0],[1,1],[1,2]]));

    # Tests for tryUp
    def test_tryUp(self):
        self.assertTrue(s.tryUp([[1,1],[1,0],[0,0],[0,1]]));
        self.assertTrue(s.tryUp([[1,0],[2,0],[3,0]]));
        self.assertTrue(s.tryUp([[1,0],[1,1],[1,2]]));
        self.assertFalse(s.tryUp([[0,1],[0,2],[0,3]]));
        self.assertFalse(s.tryUp([[0,1],[1,1],[1,2]]));
        self.assertFalse(s.tryUp([[1,1],[1,0],[0,0],[0,1],[0,2]]));
    
    # Tests for tryRight
    def test_tryRight(self):
        self.assertTrue(s.tryRight(2, [[0,1],[1,1],[1,2]]))
        self.assertTrue(s.tryRight(2, [[0,1],[1,1],[1,2],[0,2]]))
        self.assertTrue(s.tryRight(2, [[3,0],[2,0],[1,0]]))
        self.assertFalse(s.tryRight(2, [[0,2],[0,1],[1,1],[1,2]]))
        self.assertFalse(s.tryRight(2, [[1,1],[2,1],[2,2],[1,2],[0,2]]))
        self.assertFalse(s.tryRight(3, [[0,3],[0,2],[0,1],[0,0]]))
        
    # Tests for tryDown
    def test_tryDown(self):
        self.assertTrue(s.tryDown(2, [[0,1],[0,2],[1,2]]))
        self.assertTrue(s.tryDown(2, [[0,1],[0,2],[1,2],[1,1]]))
        self.assertTrue(s.tryDown(3, [[2,0],[1,0],[0,0]]))
        self.assertFalse(s.tryDown(3, [[0,2],[0,1],[1,1],[1,2],[1,3]]))
        self.assertFalse(s.tryDown(2, [[1,1],[2,1],[2,2],[1,2],[0,2]]))
        self.assertFalse(s.tryDown(3, [[3,0],[3,1],[3,2],[3,3]]))

        