
class Category:
    def __init__(self, id=None, name=None, description=None):
        self.id = id
        self.name = name
        self.description = description
    
    def getId(self):
        return self.id
    
    def getName(self):
        return self.name
    
    def getDescription(self):
        return self.description
    
    def toMap(self):
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description
        }
    
    def toArray(self):
        return [self.id, self.name, self.description]
