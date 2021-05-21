import unittest

# Implement the below function and run this file
# Return the output, No need read input or print the ouput


def floor(n1, n2):
    return(n1//n2)


# DO NOT TOUCH THE BELOW CODE
class TestFloor(unittest.TestCase):

    def test_01(self):
        self.assertEqual(floor(3, 5), 0)

    def test_02(self):
        self.assertEqual(floor(12.5, 10.5), 1.0)

    def test_03(self):
        self.assertEqual(floor(338, 44), 7)


if __name__ == '__main__':
    unittest.main(verbosity=2)
