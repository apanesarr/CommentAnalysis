class Regex:
    single = {"py" : "#", "java":"\/\/","js":"\/\/"}
    multiStart = {"py" : "'''", "java": "/\*", "js":"/\*"}
    multiEnd = {"py" : "'''", "java": "\*/", "js": "\*/"}
    
    def get(self,extension):
        return self.single[extension]
    def start(self,extension):
        return self.multiStart[extension]
    def end(self,extension):
        return self.multiEnd[extension]