
class Product:
    def __init__(self, id=None, name=None, description=None, price=None, created=None):
        self.id = id
        self.name = name
        self.description = description
        self.price = price
        self.created = created
    
    def getId(self):
        return self.id
    
    def getName(self):
        return self.name
    
    def getDescription(self):
        return self.description
    
    def getPrice(self):
        return self.price
    
    def getCreated(self):
        return self.created
    
    def toMap(self):
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "price": self.price,
            "created": self.created
        }
    
    def toArray(self):
        return [self.id, self.name, self.description, self.price, self.created]
