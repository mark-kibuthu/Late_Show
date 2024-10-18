# routes.py
from flask import request, jsonify
from app import app
from models import db, Episode, Guest, Appearance

@app.route('/episodes', methods=['GET'])
def get_episodes():
    episodes = Episode.query.all()
    return jsonify([episode.to_dict() for episode in episodes]), 200

@app.route('/episodes/<int:id>', methods=['GET'])
def get_episode_by_id(id):
    episode = Episode.query.get(id)
    
    if episode:
        return jsonify({
            'id': episode.id,
            'date': episode.date,
            'number': episode.number,
            'appearances': [
                {
                    "id": appearance.id,
                    "rating": appearance.rating,
                    "guest_id": appearance.guest_id,
                    "episode_id": appearance.episode_id,
                    "guest": appearance.guest.to_dict()
                } for appearance in episode.appearances
            ]
        }), 200

    return jsonify({'error': 'Episode not found'}), 404

@app.route('/guests', methods=['GET'])
def get_guests():
    guests = Guest.query.all()
    return jsonify([guest.to_dict() for guest in guests]), 200

@app.route('/appearances', methods=['POST'])
def create_appearance():
    data = request.get_json()

    # Validate the request data
    if not data:
        return jsonify({"errors": ["No input data provided"]}), 400

    rating = data.get('rating')
    episode_id = data.get('episode_id')
    guest_id = data.get('guest_id')

    # Check that required fields are present
    if rating is None or episode_id is None or guest_id is None:
        return jsonify({"errors": ["rating, episode_id, and guest_id are required"]}), 400

    # Validate rating range
    if not (1 <= rating <= 5):
        return jsonify({"errors": ["Rating must be between 1 and 5"]}), 400

    # Ensure the episode and guest exist
    episode = Episode.query.get(episode_id)
    guest = Guest.query.get(guest_id)
    
    if not episode:
        return jsonify({"errors": ["Episode not found"]}), 404

    if not guest:
        return jsonify({"errors": ["Guest not found"]}), 404

    # Create the new Appearance
    new_appearance = Appearance(
        rating=rating,
        episode_id=episode_id,
        guest_id=guest_id,
        air_date=data.get('air_date')  # Optional field
    )
    
    try:
        db.session.add(new_appearance)
        db.session.commit()

        # Format response data correctly
        response_data = {
            "id": new_appearance.id,
            "rating": new_appearance.rating,
            "guest_id": guest.id,
            "episode_id": episode.id,
            "episode": {
                "date": episode.date,
                "id": episode.id,
                "number": episode.number
            },
            "guest": {
                "id": guest.id,
                "name": guest.name,
                "occupation": guest.occupation
            }
        }

        return jsonify(response_data), 201

    except Exception as e:
        db.session.rollback()
        return jsonify({"errors": ["Error creating appearance"]}), 500

