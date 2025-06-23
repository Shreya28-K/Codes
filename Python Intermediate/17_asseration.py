import unittest
def reverse_string(s):
    return s[::-1]
def capitalize_string(s):
    return s.capitalize()
def is_capitalized(s):
    return s[0].isupper()
class TestStringUtils(unittest.TestCase):
  def test1(self):
    result=reverse_string("cba")
    self.assertEqual(result,"abc")
  def test2(self):
    result1=capitalize_string("shree")
    self.assertEqual(result1,"Shree")
  def test3(self):
    result2=is_capitalized("hero")
    result3=is_capitalized("HERO")
    
    self.assertFalse(result2)
    self.assertTrue(result3)



if __name__=='__main__':
  unittest.main()