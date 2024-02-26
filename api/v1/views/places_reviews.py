#!/usr/bin/python3
"""
Module Docs
"""
from api.v1.views import app_views
from flask import abort, jsonify, request
from models import storage
from models.review import Review


@app_views.route('/places/<place_id>/reviews/', methods=['GET'],
                 strict_slashes=False)
def list_reviews_of_place(place_id):
    """
    Retrieve a list of all reviews associated with a place
    """
    place = storage.get('Place', place_id)
    if not place:
        abort(404)

    reviews = [review.to_dict() for review in place.reviews]
    return jsonify(reviews)


@app_views.route('/places/<place_id>/reviews', methods=['POST'],
                 strict_slashes=False)
def create_review(place_id):
    """
    Create a new review associated with a place
    """
    data = request.get_json()
    if not data:
        abort(400, 'Request body must be JSON')

    user_id = data.get('user_id')
    text = data.get('text')

    if not user_id:
        abort(400, 'Missing user_id in request')
    if not text:
        abort(400, 'Missing text in request')

    place = storage.get('Place', place_id)
    if not place:
        abort(404)

    user = storage.get('User', user_id)
    if not user:
        abort(404)

    new_review = Review(text=text, place_id=place_id, user_id=user_id)
    storage.new(new_review)
    storage.save()

    return jsonify(new_review.to_dict()), 201


@app_views.route('/reviews/<review_id>', methods=['GET'],
                 strict_slashes=False)
def get_review(review_id):
    """
    Retrieve a specific review by its ID
    """
    review = storage.get('Review', review_id)
    if not review:
        abort(404)

    return jsonify(review.to_dict())


@app_views.route('/reviews/<review_id>', methods=['DELETE'],
                 strict_slashes=False)
def delete_review(review_id):
    """
    Delete a specific review by its ID
    """
    review = storage.get('Review', review_id)
    if not review:
        abort(404)

    storage.delete(review)
    storage.save()

    return jsonify({}), 200


@app_views.route('/reviews/<review_id>', methods=['PUT'],
                 strict_slashes=False)
def update_review(review_id):
    """
    Update a specific review by its ID
    """
    review = storage.get('Review', review_id)
    if not review:
        abort(404)

    data = request.get_json()
    if not data:
        abort(400, 'Request body must be JSON')

    text = data.get('text')
    if text:
        review.text = text

    storage.save()

    return jsonify(review.to_dict()), 200
