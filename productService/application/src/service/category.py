
from flask import request
import repository.category as RC
from configuration.security import generate
from utility.encryption import Encrypt
from model.category import Category

def add():
    data = dict(request.get_json())
    name, description = data['name'], data['description']
    return RC.add(name, description)

def addProductCategory():
    data = dict(request.get_json())
    productId, categoryId = data['product_id'], data['category_id']
    return RC.addProductCategory(productId, categoryId)

def get():
    result = False
    data = dict(request.get_json())
    categoryId = data['category_id']
    try:
        result = RC.get(categoryId)
    except: pass
    return result

def getRange(start, qnt):
    result = False
    try:
        result = RC.getRange(start, qnt)
    except: pass
    return result

def getNameRange(start, qnt):
    result = False
    name = request.args.get("name") if request.args.get("name") != None else ""
    try:
        result = RC.getNameRange(name, start, qnt)
    except: pass
    return result

def getProductRange(start, qnt):
    result = False
    data = dict(request.get_json())
    categoryId = data['category_id']
    try:
        result = RC.getProductRange(categoryId, start, qnt)
    except: pass
    return result

def update():
    result = False
    data = dict(request.get_json())
    try:
        result = RC.update(Category(**data))
    except: pass
    return result

def delete():
    data = dict(request.get_json())
    categoryId = data['category_id']
    return RC.delete(categoryId)

def deleteProductCategory():
    data = dict(request.get_json())
    id, productId, categoryId = data['id'], data['product_id'],data['category_id']
    return RC.deleteProductCategory(id, productId, categoryId)