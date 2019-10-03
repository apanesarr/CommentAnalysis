from input import Input
from comment import Comment

def main():
    file = Input().get()
    get = Comment(file["content"],file["extension"])
    print("Total # of lines: " + str(file["lines"]))
    print("Total # of comment lines: " + get.commentLines())
    print("Total # of single line comments: " + get.singleLines())
    print("Total # of comment lines within block comments: " + get.blockLines())
    print("Total # of block line comments: " + get.blockComments())
    print("Total # of TODO’s: " + get.TODOLines())
    
if __name__=="__main__":
    main()
