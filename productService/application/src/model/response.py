
class Response:
    def __init__(self, code=200, content={}):
        self.code = code
        self.content = content
    
    def toMap(self):
        return {
            "response": self.code,
            "content": self.content
        }