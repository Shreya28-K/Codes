import unittest
def add(a,b):
  return a+b
class Test_add(unittest.TestCase):
  def test_add(self):
    result=add(3,4)
    expected=7
    self.assertEqual(result,expected)

if __name__ =='__main__':
  unittest.main()