import re

class FalsePositive:
    content: str

    def __init__(self,content):
        self.content = content
     
    def falsePositives(self, symbol):
        pattern = "(\(|(\"))(.*)" + str(symbol) + "(.*)(\)|(\"))\n"
        #fsm : https://drive.google.com/open?id=13OBCUdiG8ITYOYQzTuiDQUkA9P0SMlga
        result = re.findall(pattern,self.content)
        return result   
    
    def lines(self,symbol):
        count = 0
        # returned object from re.findall has no function len so thats why theres a for loop
        for f in self.falsePositives(symbol):
            count+=1
        return count