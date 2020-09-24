
from flask import request
import repository.product as RP
from configuration.security import generate
from utility.encryption import Encrypt
from model.product import Product

def add():
    data = dict(request.get_json())
    name, description, price = data['name'], data['description'], data['price']
    return RP.add(name, description, price)

def addDiscount():
    data = dict(request.get_json())
    productId, state, deadline, porcentage = data['product_id'], data['state'], data['deadline'], data["porcentage"]
    return RP.addDiscount(productId, state, deadline, porcentage)

def get():
    result = False
    data = dict(request.get_json())
    productId = data['product_id']
    try:
        result = RP.get(productId)
    except: pass
    return result

def getProductSize():
    result = False
    try:
        result = RP.getProductSize()
    except: pass
    return result

def getDiscount():
    result = False
    data = dict(request.get_json())
    discountId = data['discount_id']
    try:
        result = RP.getDiscount(discountId)
    except: pass
    return result

def getProductDiscountRange(start, qnt):
    result = False
    try:
        result = RP.getProductDiscountRange(start, qnt)
    except: pass
    return result

def getProductDiscount():
    result = False
    data = dict(request.get_json())
    productId = data['product_id']
    try:
        result = RP.getProductDiscount(productId)
    except: pass
    return result

def getProductArrayDiscount():
    result = False
    data = dict(request.get_json())
    productIds = data['products']
    try:
        result = RP.getProductArrayDiscount(productIds)
    except: pass
    return result

def getProductArray():
    result = False
    data = dict(request.get_json())
    productIds = data['products']
    try:
        result = RP.getProductArray(productIds)
    except: pass
    return result

def getRange(start, qnt):
    result = False
    try:
        result = RP.getRange(start, qnt)
    except: pass
    return result

def getProductAll():
    result = False
    try:
        result = RP.getProductAll()
    except: pass
    return result

def getDateRange(start, qnt):
    result = False
    data = dict(request.get_json())
    date = data['date']
    try:
        result = RP.getDateRange(date, start, qnt)
    except: pass
    return result

def getDiscountRange(start, qnt):
    result = False
    try:
        result = RP.getDiscountRange(start, qnt)
    except: pass
    return result

def getNameRange(start, qnt):
    result = False
    name = request.args.get("name") if request.args.get("name") != None else ""
    try:
        result = RP.getNameRange(name, start, qnt)
    except: pass
    return result

def update():
    result = False
    data = dict(request.get_json())
    try:
        result = RP.update(Product(**data))
    except: pass
    return result

def updateState():
    result = False
    data = dict(request.get_json())
    productId = data['product_id']
    try:
        result = RP.updateState(productId)
    except: pass
    return result

def updateDiscountState():
    result = False
    data = dict(request.get_json())
    discountId = data['discount_id']
    try:
        result = RP.updateDiscountState(discountId)
    except: pass
    return result

def delete():
    data = dict(request.get_json())
    productId = data['product_id']
    return RP.delete(productId)

def deleteDiscount():
    data = dict(request.get_json())
    discountId = data['discount_id']
    return RP.deleteDiscount(discountId)