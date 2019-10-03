import re
from regex import Regex

class Single:
    content: str
    symbol: str

    def __init__(self,content,extension):
        self.content = content
        self.symbol = Regex().get(extension)

    def comments(self):
        pattern = str(self.symbol) + "(.*)\n"
        #fsm : https://drive.google.com/open?id=1yX79U4SEQpeR2YEX-UpDCm5JuJgERQvO
        result = re.findall(pattern, self.content) #finds all regex matches
        return result

    def lines(self):
        return int(len(self.comments()))

    def falsePositives(self):
        pattern = "(\(|(\"))" + str(self.symbol) + "(.*)(\)|(\"))\n"
        #fsm : https://drive.google.com/open?id=1mHKnjHiEm1m3QrX4Ta7DK9HyZ6tRdfPN
        result = re.findall(pattern,self.content)
        return result        
    
    def falsePositivesLines(self):
        count = 0
        # returned object from re.findall has no function len so thats why theres a for loop
        # could be optimized 
        for f in self.falsePositives():
            count+=1
        return count
    
    def multiSingleBlocks(self):
        count = 0
        for f in self.multiSingles():
            count+=1 
        return count

    def multiSingles(self):
        pattern = "(" + str(self.symbol) + "(.*)(\n))(((\t| )*)"+ str(self.symbol)+ "(.*)(\n))+"
        #fsm : https://drive.google.com/open?id=1Lfa6S313mNqqNOGOoJruvgBJJ3nloXzq
        result = re.finditer(pattern, self.content) 
        return result

    def multiSingleLines(self):
        count = 0
        for f in self.multiSingles():
            count+=len(f[0].strip().split("\n")) 
        return count
        