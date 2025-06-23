import unittest
class CoffeeMenu:
  def __init__(self):
    self.menu = {
      'espresso': 2.50,
      'latte': 2.75,
      'cappuccino': 3.20,
      'americano': 2.70
    }
  def get_price(self,str):
    return self.menu.get(str.lower(),None)

class TestMenu(unittest.TestCase):
  def setUp(self):
    self.m=CoffeeMenu()
  def tearDown(self):
    self.m=None
  def test1(self):
    self.assertEqual(self.m.get_price('latte'),2.75)
  def test2(self):
    self.assertIsNone(self.m.get_price('mocha')) # return passed if not found
    
if __name__=="__main__":
  unittest.main()