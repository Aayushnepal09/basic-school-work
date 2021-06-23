import unittest
from arithmetic import*
class Test_Arithmetic(unittest.TestCase):
    def setUp(self):
        self.a=Arithmetic()

    def test_add(self):
        self.assertEqual(6,self.a.add(3,3))

    def test_sub(self):
        self.assertEqual(0,self.a.sub(5,5))

    def test_mul(self):
        self.assertEqual(30,self.a.mul(5,5))

    def test_assert(self):
    #self.assertRaises(value error, self.a.div,10,0)
     with self.assertRaises(ValueError):
         self.a.div(4,0)
