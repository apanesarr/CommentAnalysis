import sys

class Input:
    def content(self,filename):
        data = ""
        with open(filename, 'r') as myfile:
            data = myfile.read()
        return data

    def get(self):
        #sys.argv also counts running file
        if len(sys.argv)==2:
            file = {}
            filename = str(sys.argv[1])
            input = filename.split('.')
            file["name"] = input[0]
            file["extension"] = input[1]
            file["content"] = self.content(filename)
            file["lines"] = int(len(file["content"].split("\n")))
            return file
        else:
            print("Error only 1 argument is allowed")