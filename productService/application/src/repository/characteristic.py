
from configuration.app import db

def add(name, content):
    result = False
    try:
        tmp = db.procedure("addCharacteristic", [name, content])
        result = tmp[0]["rows"]
    except: pass
    return result

def addCharacteristicProduct(productId, charactId):
    result = False
    try:
        tmp = db.procedure("addCharacteristicProduct", [charactId, productId])
        result = tmp[0]["rows"]
    except: pass
    return result

def get(charactId):
    qry = "SELECT * FROM characteristic WHERE id = {}".format(charactId)
    result = db.fetchOne(qry)
    return result

def getProductCharacteristic(productId):
    qry = "SELECT c.* FROM characteristic c INNER JOIN product_characteristic pc ON (pc.charact_id = c.id) WHERE pc.product_id = {}".format(productId)
    result = db.fetchOne(qry)
    return result

def update(characterictics):
    result = False
    try:
        tmp = db.procedure("updateCharacteristic", characterictics.toArray())
        result = tmp[0]["rows"] > 0
    except: pass
    return result

def delete(charactId):
    result = False
    try:
        tmp = db.procedure("deleteCharacteristic", [charactId])
        result = tmp[0]["rows"] > 0
    except: pass
    return result

def deleteProductCharacteristic(id=0, productId=0, charactId=0):
    result = False
    try:
        tmp = db.procedure("deleteProductCharacteristic", [id, productId, charactId])
        result = tmp[0]["rows"] > 0
    except: pass
    return result