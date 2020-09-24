
from flask import request
import repository.characteristic as RC
from configuration.security import generate
from utility.encryption import Encrypt
from model.characteristic import Characteristic

def add():
    data = dict(request.get_json())
    name, content = data['name'], data['content']
    return RC.add(name, str(content).replace("'", '"'))

def addCharacteristicProduct():
    data = dict(request.get_json())
    productId, charactId = data['product_id'], data['charact_id']
    return RC.addCharacteristicProduct(productId, charactId)

def get(charactId):
    result = False
    data = dict(request.get_json())
    charactId = data['charact_id']
    try:
        result = RC.get(charactId)
    except: pass
    return result

def getProductCharacteristic():
    result = False
    data = dict(request.get_json())
    productId = data['product_id']
    try:
        result = RC.getProductCharacteristic(productId)
    except: pass
    return result

def update():
    result = False
    data = dict(request.get_json())
    try:
        result = RC.update(Characteristic(**data))
    except: pass
    return result

def delete():
    data = dict(request.get_json())
    charactId = data['charact_id']
    return RC.delete(charactId)

def deleteProductCharacteristic():
    data = dict(request.get_json())
    id, productId, charactId = data['id'], data['product_id'], data['charact_id']
    return RC.deleteProductCharacteristic(discountId)