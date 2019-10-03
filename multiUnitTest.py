import unittest
from multi import Multi
from regex import Regex

class TestMulti(unittest.TestCase):

    def test_regex(self):
        symbol = Regex().start("js")
        self.assertEqual("/\*", str(symbol))
   
    def test_multiLineComment(self):
        string = "\'\'\'Comment\'\'\'"
        test = Multi(string,"py")
        output = test.blocks()
        self.assertEqual(1, output)
   
    def test_multiLineCommentsWithNewLines(self):
        string = "\'\'\'\nComment\n\'\'\'"
        test = Multi(string,"py")
        output = test.blocks()
        self.assertEqual(1, output)

    def test_numOfMultiLineComments(self):
        string = "\'\'\'\nComment\n\'\'\'"
        test = Multi(string,"py")
        output = test.lines()
        self.assertEqual(3, output)        
    
    def test_falsePositive(self):
        string = "print(\'\'\' Hello \'\'\')"
        test = Multi(string,"py")
        output = test.lines()
        self.assertEqual(1, output)

if __name__ == '__main__':
    unittest.main()