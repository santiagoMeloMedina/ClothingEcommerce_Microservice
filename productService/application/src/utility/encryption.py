
from passlib.context import CryptContext

class Encrypt:
    def __init__(self, hash=""):
        self.__context = CryptContext(
            schemes=["pbkdf2_sha256"],
            default="pbkdf2_sha256",
            pbkdf2_sha256__default_rounds=30000
        )
        self.__string = hash
    
    def setString(self, hash):
        self.__string = hash
        return self
    
    def getString(self):
        return self.__string
    
    def encrypt(self, password):
        self.__string = self.__context.encrypt(password)
        return self
    
    def validate(self, password):
        return self.__context.verify(password, self.__string)