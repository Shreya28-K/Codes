import unittest
class Calculator:
  def add(self,a,b):
    return a+b
  def sub(self,a,b):
    return a-b
class TestCaseCal(unittest.TestCase):
  def setUp(self):
    self.cal=Calculator()
  def tearDown(self):
    self.cal=None
  def test1(self):
    self.assertEqual(self.cal.add(4,3),7)
  def test2(self):
    self.assertEqual(self.cal.sub(4,3),1)

if __name__=="__main__":
  unittest.main()
    


  