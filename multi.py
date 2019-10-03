import re 
from regex import Regex
from false_positive import FalsePositive

class Multi:
    content: str
    start: str
    end: str
    falsePositive: FalsePositive
    
    def __init__(self,content,extension):
        self.content = content
        self.start = Regex().start(extension)
        self.end = Regex().end(extension)
        self.falsePositive = FalsePositive(content)
    
    def comments(self):
        pattern = "(?s)" + str(self.start) + ".*?" + str(self.end)
        #fsm : https://drive.google.com/open?id=1xSeuRl_yGx1NeHGfmlgwiJejTN2CO8qQ
        result = re.findall(pattern,self.content)
        return result
    
    def lines(self):
        count = []
        for f in self.comments():
            count.extend(f.strip().split('\n'))        
        return int(len(count)) - int(self.falsePositive.lines(self.start))
    
    def blocks(self):
        return int(len(self.comments()))- int(len(self.falsePositive.falsePositives(self.start)))