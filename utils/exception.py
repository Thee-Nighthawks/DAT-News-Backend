class UnknownDBError(Exception):
    # Constructor or Initializer
    def __init__(self, moduleName):
        self.moduleName = moduleName
    # __str__ is to print() the value
    def __str__(self):
        return("DB Error while accessing MongoDB in module: ", self.moduleName)

class UnknownPlatform(Exception):
    # Constructor or Initializer
    def __init__(self, moduleName):
        self.moduleName = moduleName
    # __str__ is to print() the value
    def __str__(self):
        return("Unknown Platform (OS): ", self.moduleName)  