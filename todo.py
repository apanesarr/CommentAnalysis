import re
from false_positive import FalsePositive

class TODO:
    content: str
    falsePositive: FalsePositive
    
    def __init__(self,content):
        self.content = content
        self.falsePositive = FalsePositive(content)
   
    def todo(self):
        pattern = "TODO"
        result = re.findall(pattern,self.content)
        return result
    
    def lines(self):
        return(int(len(self.todo()))- int(self.falsePositive.lines("TODO")))