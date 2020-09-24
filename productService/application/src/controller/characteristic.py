
from flask import Blueprint, request, jsonify
from configuration.auth import system, user, admin
import service.characteristic as SC

alias = "charact"

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
def addCharacteristicProduct():
    response = {"response": 400, "content": {}}
    result = SC.addCharacteristicProduct()
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

@controller.route("/{}/get/product".format(alias), methods=["POST"])
@system
def getProductCharacteristic():
    response = {"response": 400, "content": {}}
    data = SC.getProductCharacteristic()
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
def deleteProductCharacteristic():
    response = {"response": 400, "content": {}}
    result = SC.deleteProductCharacteristic()
    if result:
        response = {"response": 200, "content": True}
    return jsonify(response)

