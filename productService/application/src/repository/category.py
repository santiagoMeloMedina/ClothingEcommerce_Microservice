
from configuration.app import db

def add(name, description):
    result = False
    try:
        tmp = db.procedure("addCategory", [name, description])
        result = tmp[0]["rows"]
    except: pass
    return result

def addProductCategory(productId, categoryId):
    result = False
    try:
        tmp = db.procedure("addProductCategory", [productId, categoryId])
        result = tmp[0]["rows"]
    except: pass
    return result

def get(categoryId):
    qry = "SELECT * FROM category WHERE id='{}'".format(categoryId)
    result = db.fetchOne(qry)
    return result

def getRange(start, qnt):
    qry = "SELECT * FROM category LIMIT {},{}".format(start, qnt)
    result = db.fetchAll(qry)
    return result

def getNameRange(name, start, qnt):
    qry = "SELECT * FROM category WHERE name LIKE '{}%' LIMIT {},{}".format(name, start, qnt)
    result = db.fetchAll(qry)
    return result

def getProductRange(categoryId, start, qnt):
    qry = """SELECT p.* FROM product p INNER JOIN product_category pc 
            ON (pc.product_id=p.id) WHERE pc.category_id={} LIMIT {},{}""".format(categoryId, start, qnt)
    result = db.fetchAll(qry)
    return result

def update(category):
    result = False
    try:
        tmp = db.procedure("updateCategory", category.toArray())
        result = tmp[0]["rows"] > 0
    except: pass
    return result

def delete(categoryId):
    result = False
    try:
        tmp = db.procedure("deleteCategory", [categoryId])
        result = tmp[0]["rows"] > 0
    except: pass
    return result

def deleteProductCategory(id=0, productId=0, categoryId=0):
    result = False
    try:
        tmp = db.procedure("deleteProductCategory", [id, productId, categoryId])
        result = tmp[0]["rows"] > 0
    except: pass
    return result