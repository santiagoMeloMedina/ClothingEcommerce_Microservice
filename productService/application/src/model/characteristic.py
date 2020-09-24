
class Characteristic:
    def __init__(self, id=None, name=None, content=None):
        self.id = id
        self.name = name
        self.content = content
    
    def getId(self):
        return self.id
    
    def getName(self):
        return self.name
    
    def getContent(self):
        return self.content
    
    def toMap(self):
        return {
            "id": self.id,
            "name": self.name,
            "content": self.content
        }
    
    def toArray(self):
        return [self.id, self.name, str(self.content).replace("'", '"')]
