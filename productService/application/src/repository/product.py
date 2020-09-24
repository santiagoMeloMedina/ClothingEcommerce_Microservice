
from configuration.app import db

def add(name, description, price):
    result = False
    try:
        tmp = db.procedure("addProduct", [name, description, price])
        result = tmp[0]["rows"]
    except: pass
    return result

def addDiscount(productId, state, deadline, porcentage):
    result = False
    try:
        tmp = db.procedure("addDiscount", [productId, state, deadline, porcentage])
        result = tmp[0]["rows"]
    except: pass
    return result

def get(productId):
    qry = "SELECT * FROM product WHERE id='{}'".format(productId)
    result = db.fetchOne(qry)
    return result

def getProductSize():
    qry = "SELECT COUNT(*) as count FROM product"
    result = db.fetchOne(qry)
    return result

def getDiscount(discountId):
    qry = "SELECT * FROM discount WHERE id='{}'".format(discountId)
    result = db.fetchOne(qry)
    return result

def getProductDiscountRange(start, qnt):
    qry = "SELECT p.* FROM product p INNER JOIN discount d ON (d.product_id = p.id) WHERE d.state = true ORDER BY d.porcentage DESC LIMIT {},{}".format(start, qnt)
    result = db.fetchAll(qry)
    return result

def getProductDiscount(productId):
    qry = "SELECT * FROM discount WHERE product_id='{}'".format(productId)
    result = db.fetchAll(qry)
    return result

def getProductArrayDiscount(productIds):
    ids = " OR ".join(["product_id={}".format(pid) for pid in productIds])
    qry = "SELECT * FROM discount WHERE {}".format(ids)
    result = db.fetchAll(qry)
    return result

def getProductArray(productIds):
    ids = " OR ".join(["id={}".format(pid) for pid in productIds])
    qry = "SELECT * FROM product WHERE {}".format(ids)
    result = db.fetchAll(qry)
    return result

def getDateRange(date, start, qnt):
    qry = "SELECT * FROM product WHERE created <= '{}' ORDER BY created DESC LIMIT {},{}".format(date, start, qnt)
    result = db.fetchAll(qry)
    return result

def getRange(start, qnt):
    qry = "SELECT * FROM product LIMIT {},{}".format(start, qnt)
    result = db.fetchAll(qry)
    return result

def getProductAll():
    qry = "SELECT id, name FROM product"
    result = db.fetchAll(qry)
    return result

def getDiscountRange(start, qnt):
    qry = """SELECT d.id as did, p.id as pid, d.state, d.deadline, d.porcentage, p.name, p.description, p.price, p.created, p.active 
                FROM discount d INNER JOIN product p ON p.id = d.product_id LIMIT {}, {}""".format(start, qnt)
    result = db.fetchAll(qry)
    return result

def getNameRange(name, start, qnt):
    qry = "SELECT * FROM product WHERE name LIKE '{}%' LIMIT {},{}".format(name, start, qnt)
    result = db.fetchAll(qry)
    return result

def update(product):
    result = False
    try:
        tmp = db.procedure("updateProduct", product.toArray())
        result = tmp[0]["rows"] > 0
    except: pass
    return result

def updateState(productId):
    result = False
    try:
        tmp = db.procedure("updateProductState", [productId])
        result = tmp[0]["rows"] > 0
    except: pass
    return result

def updateDiscountState(discountId):
    result = False
    try:
        tmp = db.procedure("updateDiscountState", [discountId])
        result = tmp[0]["rows"] == 0 or tmp[0]["rows"] == 1
    except: pass
    return result

def delete(productId):
    result = False
    try:
        tmp = db.procedure("deleteProduct", [productId])
        result = tmp[0]["rows"] > 0
    except: pass
    return result

def deleteDiscount(discountId):
    result = False
    try:
        tmp = db.procedure("deleteDiscount", [discountId])
        result = tmp[0]["rows"] > 0
    except: pass
    return result