import unittest
from single import Single
from regex import Regex

class TestSingle(unittest.TestCase):

    def test_regex(self):
        symbol = Regex().start("java")
        self.assertEqual("/\*", str(symbol))

    def test_singleComment(self):
        string = "#Comment\n"
        test = Single(string,"py")
        numOfSingleComments = test.lines()
        self.assertEqual(1, numOfSingleComments)
    
    def test_besideSingleComment(self):
        string = "print(\"Hello\") #Comment\n"
        test = Single(string,"py")
        numOfSingleComments = test.lines()
        self.assertEqual(1, numOfSingleComments)
    
    def test_twoSingleCommentsAsBlock(self):
        string = "#Comment1\n#Comment2\n"
        test = Single(string,"py")
        numOfSingleComments = test.multiSingleBlocks()
        self.assertEqual(1, numOfSingleComments)

    def test_linesInBlock(self):
        string = "#Comment1\n#Comment2\n"
        test = Single(string,"py")
        numOfSingleComments = test.multiSingleLines()    
        self.assertEqual(2, int(numOfSingleComments))

    def test_falsePositive(self):
        string = "print(\"#Hello\")\n"   
        test = Single(string,"py")
        numOfSingleComments = test.falsePositivesLines()    
        self.assertEqual(1, int(numOfSingleComments))        

if __name__ == '__main__':
    unittest.main()