import unittest
import math

def get_sqrt(n):
  return math.sqrt(n)

def divide(a, b):
  return a / b

class Testcase(unittest.TestCase):
  def test1(self):
       
    with self.assertRaises(ValueError):
      r1=get_sqrt(-144)


      
     
  def test2(self):
    with self.assertRaises(ZeroDivisionError):
      divide(144,0)


if  __name__ =="__main__":
  unittest.main()
