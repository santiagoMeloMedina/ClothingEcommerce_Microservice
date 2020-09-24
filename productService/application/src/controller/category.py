
from flask import Blueprint, request, jsonify
from configuration.auth import system, user, admin
import service.category as SC

alias = "category"

controller = Blueprint(alias, __name__)

@controller.route("/{}/add".format(alias), methods=["POST"])
@system
@admin
def add():
    response = {"response": 400, "content": {}}
    result = SC.add()
    if result:
        response = {"response": 200, "content": result}
    return jsonify(response)

@controller.route("/{}/add/product".format(alias), methods=["POST"])
@system
@admin
def addProductCategory():
    response = {"response": 400, "content": {}}
    result = SC.addProductCategory()
    if result:
        response = {"response": 200, "content": result}
    return jsonify(response)

@controller.route("/{}/get".format(alias), methods=["POST"])
@system
def get():
    response = {"response": 400, "content": {}}
    data = SC.get()
    if data:
        response = {"response": 200, "content": data}
    return jsonify(response)

@controller.route("/{}/get/<int:start>/<int:qnt>".format(alias), methods=["GET"])
@system
def getRange(start, qnt):
    response = {"response": 400, "content": {}}
    data = SC.getRange(start, qnt)
    if data:
        response = {"response": 200, "content": data}
    return jsonify(response)

@controller.route("/{}/get/name/<int:start>/<int:qnt>".format(alias), methods=["GET"])
@system
def getNameRange(start, qnt):
    response = {"response": 400, "content": {}}
    data = SC.getNameRange(start, qnt)
    if data:
        response = {"response": 200, "content": data}
    return jsonify(response)

@controller.route("/{}/get/product/<int:start>/<int:qnt>".format(alias), methods=["POST"])
@system
def getProductRange(start, qnt):
    response = {"response": 400, "content": {}}
    data = SC.getProductRange(start, qnt)
    if data:
        response = {"response": 200, "content": data}
    return jsonify(response)

@controller.route("/{}/update".format(alias), methods=["PUT"])
@system
@admin
def update():
    response = {"response": 400, "content": {}}
    result = SC.update()
    if result:
        response = {"response": 200, "content": True}
    return jsonify(response)

@controller.route("/{}/delete".format(alias), methods=["DELETE"])
@system
@admin
def delete():
    response = {"response": 400, "content": {}}
    result = SC.delete()
    if result:
        response = {"response": 200, "content": True}
    return jsonify(response)

@controller.route("/{}/delete/product".format(alias), methods=["DELETE"])
@system
@admin
def deleteProductCategory():
    response = {"response": 400, "content": {}}
    result = SC.deleteProductCategory()
    if result:
        response = {"response": 200, "content": True}
    return jsonify(response)


