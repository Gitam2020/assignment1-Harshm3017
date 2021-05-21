import unittest


def add(n1,n2):

    return(n1+n2)



# DO NOT TOUCH THE BELOW CODE
class TestAdd(unittest.TestCase):

    def test_01(self):
        self.assertEqual(add(3, 5), 8)

    def test_02(self):
        self.assertEqual(add(12, 10), 22)

    def test_03(self):
        self.assertEqual(add(33, 44), 77)


if __name__ == '__main__':
    unittest.main(verbosity=2)
