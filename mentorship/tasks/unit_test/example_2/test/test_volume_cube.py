import unittest
from example_2.volume_cube import volume_of_cube

class TestCuboid(unittest.TestCase):

    def test_volume(self):
        self.assertAlmostEqual(volume_of_cube(2), 8, msg="Este es el testing")