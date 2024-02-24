#!/usr/bin/python3
""" States part API """
from api.v1.views import app_views
from flask import jsonify, abort, request
from models import storage
from models.state import State


@app_views.route('/states', methods=['GET'], strict_slashes=False)
def GetStates():
    """ Get a list of available states objects """
    StatesData = storage.all(State)
    return jsonify([obj.to_dict() for obj in StatesData.values()])


@app_views.route('/states/<state_id>', methods=['GET'], strict_slashes=False)
def GetStateById(state_id):
    """ Get a state object by its id """
    state = storage.get("State", state_id)
    if not state:
        abort(404)
    return jsonify(state.to_dict())


@app_views.route('/states/<state_id>',
                 methods=['DELETE'],
                 strict_slashes=False)
def DelState(state_id):
    """ Delete a state object by its id """
    state = storage.get("State", state_id)
    if not state:
        abort(404)
    state.delete()
    storage.save()
    return jsonify({}), 200


@app_views.route('/states', methods=['POST'], strict_slashes=False)
def CreateState():
    """ Create a new state object """
    RequestObj = request.get_json()
    if not RequestObj:
        abort(400, "Not a JSON")
    if "name" not in RequestObj:
        abort(400, "Missing name")
    state = State(**RequestObj)
    storage.new(state)
    storage.save()
    return jsonify(state.to_dict()), 201


@app_views.route('/states/<state_id>', methods=['PUT'], strict_slashes=False)
def UpdateState(state_id):
    """ update a state object """
    state = storage.get("State", state_id)
    if not state:
        abort(404)

    RequestObj = request.get_json()
    if not RequestObj:
        abort(400, "Not a JSON")

    for k, v in RequestObj.items():
        if k != 'id' and k != 'created_at' and k != 'updated_at':
            setattr(state, k, v)
    storage.save()
    return jsonify(state.to_dict()), 200
