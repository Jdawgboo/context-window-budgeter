import unittest
from tool import estimate,plan
class BudgetTests(unittest.TestCase):
 def test_plan(self):
  self.assertEqual(estimate('12345'),2);self.assertEqual(plan(['abcd','efgh','ijkl'],2)['selected'],[0,1]);self.assertEqual(plan(['abcdefgh'],1)['selected'],[])
if __name__=='__main__':unittest.main()
