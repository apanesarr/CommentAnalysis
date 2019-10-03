import unittest
from todo import TODO
from regex import Regex

class TestTODO(unittest.TestCase):

    def test_regex(self):
        symbol = Regex().start("py")
        self.assertEqual("'''", str(symbol))

    def test_todo(self):
        string = "#TODO: this test\n"
        test = TODO(string)
        output = test.lines()
        self.assertEqual(1, output)

    def test_falsePositive(self):
        string = "print(\"TODO\")"
        test = TODO(string)
        output = test.lines()
        self.assertEqual(1, output)        

if __name__ == '__main__':
    unittest.main()