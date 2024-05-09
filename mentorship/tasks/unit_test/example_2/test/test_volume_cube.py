import unittest
from example_2.volume_cube import volume_of_cube

class TestCuboid(unittest.TestCase):

    def test_volume(self):
        self.assertAlmostEqual(volume_of_cube(2), 8, msg="Este es el testing")
        self.assertAlmostEqual(volume_of_cube(1), 1)
        self.assertAlmostEqual(volume_of_cube(0), 0)
        self.assertAlmostEqual(volume_of_cube(5.5), 166.375)

    def test_input_value(self):
        self.assertRaises(TypeError, volume_of_cube, "Hello")