import unittest
from TernarySearchTree import TSTNode,TernarySearchTree

class TestTST(unittest.TestCase):
  def test_geeksforgeeks(self):
    t = TernarySearchTree()
    t.insert("cat")
    t.insert("cats")
    t.insert("up")
    t.insert("bug")
    # expect = "bug,cat,cats,up"
    # self.assertEqual(expect, str(t))
    self.assertEqual(True, t.search("cats"))
    self.assertEqual(False, t.search("bu"))
    self.assertEqual(True, t.search("cat"))

  def test_sanfoundry(self):
    print("")
    t = TernarySearchTree()
    t.insert("apple")
    t.insert("pine")
    t.insert("pineapple")
    t.insert("pin")
    t.insert("in")
    t.insert("i")
    t.insert("mango")
    t.insert("man")
    t.insert("an")
    t.insert("a")
    self.assertEqual(True,t.search("pin"))
    self.assertEqual(False,t.search("pines"))
    self.assertEqual(True,t.search("pine"))
    self.assertEqual(True,t.search("i"))
    t.delete("i")
    self.assertEqual(False,t.search("i"))
    t.delete("in")
    t.delete("apple")
    t.delete("pineapple")
    self.assertEqual(False,t.search("apple"))
    self.assertEqual(False,t.isEmpty())
    self.assertEqual(False,t.isEmpty())

    # print(t)
if __name__ == '__main__':
  unittest.main()