import unittest
import snake as s

class snakeTest(unittest.TestCase):

    # Tests for numberOfAvailableDifferentPaths
    def testAcceptanceTests(self):
        self.assertEqual(s.numberOfAvailableDifferentPaths([4, 3], [[2,2], [3,2], [3,1], [3,0], [2,0], [1,0], [0,0]], 3), 7)

    # Tests for selfIntersects
    # Tests for tryLeft
    # Tests for tryUp
    # Tests for tryRight
    # Tests for tryDown