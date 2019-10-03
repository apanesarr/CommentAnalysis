from single import Single
from multi import Multi
from todo import TODO

class Comment:
    content: str
    extension: str
    single: Single
    multi: Multi
    todo: TODO

    def __init__(self,content,extension):
        self.content = content
        self.extension = extension
        self.single = Single(self.content, self.extension)
        self.multi = Multi(self.content,self.extension)
        self.todo = TODO(self.content)

    def singleLines(self):
        singles = self.single.lines()
        multiSingles = self.single.multiSingleLines()
        falsePositives = self.single.falsePositivesLines() #special case pattern for single false positives
        return str(singles-multiSingles-falsePositives)
    
    def blockComments(self):
        blocks = self.multi.blocks()
        multiSingleBlocks = int(self.single.multiSingleBlocks())
        return str(blocks + multiSingleBlocks)

    def blockLines(self):
        lines = self.multi.lines()
        multiSingleLines = self.single.multiSingleLines()
        return str(lines + multiSingleLines)
    
    def commentLines(self):
        return str(int(self.singleLines()) + int(self.blockLines()))

    def TODOLines(self):
        return str(int(self.todo.lines()))