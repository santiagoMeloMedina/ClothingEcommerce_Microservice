
from flask import Blueprint, request, jsonify
from configuration.auth import system, user, admin
import service.product as SP

alias = "product"

controller = Blueprint(alias, __name__)

@controller.route("/{}/add".format(alias), methods=["POST"])
@system
@admin
def add():
    response = {"response": 400, "content": {}}
    result = SP.add()
    if result:
        response = {"response": 200, "content": result}
    return jsonify(response)

@controller.route("/{}/add/discount".format(alias), methods=["POST"])
@system
@admin
def addDiscount():
    response = {"response": 400, "content": {}}
    result = SP.addDiscount()
    if result:
        response = {"response": 200, "content": result}
    return jsonify(response)

@controller.route("/{}/get".format(alias), methods=["POST"])
@system
def get():
    response = {"response": 400, "content": {}}
    data = SP.get()
    if data:
        response = {"response": 200, "content": data}
    return jsonify(response)

@controller.route("/{}/get/size".format(alias), methods=["GET"])
@system
def getProductSize():
    response = {"response": 400, "content": {}}
    data = SP.getProductSize()
    if data:
        response = {"response": 200, "content": data}
    return jsonify(response)

@controller.route("/{}/get/discount".format(alias), methods=["POST"])
@system
def getDiscount():
    response = {"response": 400, "content": {}}
    data = SP.getDiscount()
    if data:
        response = {"response": 200, "content": data}
    return jsonify(response)

@controller.route("/{}/get/discount/<int:start>/<int:qnt>".format(alias), methods=["GET"])
@system
def getProductDiscountRange(start, qnt):
    response = {"response": 400, "content": {}}
    data = SP.getProductDiscountRange(start, qnt)
    if data:
        response = {"response": 200, "content": data}
    return jsonify(response)

@controller.route("/{}/get/discount/product".format(alias), methods=["POST"])
@system
def getProductDiscount():
    response = {"response": 400, "content": {}}
    data = SP.getProductDiscount()
    if data:
        response = {"response": 200, "content": data}
    return jsonify(response)

@controller.route("/{}/get/discount/product/many".format(alias), methods=["POST"])
@system
def getProductArrayDiscount():
    response = {"response": 400, "content": {}}
    data = SP.getProductArrayDiscount()
    if data:
        response = {"response": 200, "content": data}
    return jsonify(response)

@controller.route("/{}/get/product/many".format(alias), methods=["POST"])
@system
def getProductArray():
    response = {"response": 400, "content": {}}
    data = SP.getProductArray()
    if data:
        response = {"response": 200, "content": data}
    return jsonify(response)


@controller.route("/{}/get/<int:start>/<int:qnt>".format(alias), methods=["GET"])
@system
def getRange(start, qnt):
    response = {"response": 400, "content": {}}
    data = SP.getRange(start, qnt)
    if data:
        response = {"response": 200, "content": data}
    return jsonify(response)

@controller.route("/{}/get/all".format(alias), methods=["GET"])
@system
def getProductAll():
    response = {"response": 400, "content": {}}
    data = SP.getProductAll()
    if data:
        response = {"response": 200, "content": data}
    return jsonify(response)

@controller.route("/{}/get/date/<int:start>/<int:qnt>".format(alias), methods=["POST"])
@system
def getDateRange(start, qnt):
    response = {"response": 400, "content": {}}
    data = SP.getDateRange(start, qnt)
    if data:
        response = {"response": 200, "content": data}
    return jsonify(response)

@controller.route("/{}/get/discount/combined/<int:start>/<int:qnt>".format(alias), methods=["GET"])
@system
def getDiscountRange(start, qnt):
    response = {"response": 400, "content": {}}
    data = SP.getDiscountRange(start, qnt)
    if data:
        response = {"response": 200, "content": data}
    return jsonify(response)

@controller.route("/{}/get/name/<int:start>/<int:qnt>".format(alias), methods=["GET"])
@system
def getNameRange(start, qnt):
    response = {"response": 400, "content": {}}
    data = SP.getNameRange(start, qnt)
    if data:
        response = {"response": 200, "content": data}
    return jsonify(response)

@controller.route("/{}/update/state".format(alias), methods=["PUT"])
@system
@admin
def updateState():
    response = {"response": 400, "content": {}}
    result = SP.updateState()
    if result:
        response = {"response": 200, "content": True}
    return jsonify(response)

@controller.route("/{}/update/state/discount".format(alias), methods=["PUT"])
@system
@admin
def updateDiscountState():
    response = {"response": 400, "content": {}}
    result = SP.updateDiscountState()
    if result:
        response = {"response": 200, "content": True}
    return jsonify(response)

@controller.route("/{}/update".format(alias), methods=["PUT"])
@system
@admin
def update():
    response = {"response": 400, "content": {}}
    result = SP.update()
    if result:
        response = {"response": 200, "content": True}
    return jsonify(response)

@controller.route("/{}/delete".format(alias), methods=["DELETE"])
@system
@admin
def delete():
    response = {"response": 400, "content": {}}
    result = SP.delete()
    if result:
        response = {"response": 200, "content": True}
    return jsonify(response)

@controller.route("/{}/delete/discount".format(alias), methods=["DELETE"])
@system
@admin
def deleteDiscount():
    response = {"response": 400, "content": {}}
    result = SP.deleteDiscount()
    if result:
        response = {"response": 200, "content": True}
    return jsonify(response)

