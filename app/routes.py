from flask import Blueprint, jsonify

api = Blueprint('api', __name__)

# Sample Netflix summary route
@api.route('/netflix/summary', methods=['GET'])
def netflix_summary():
    data = {
        "total_titles": 7787,
        "most_common_genre": "Documentaries",
        "country_with_most_content": "United States"
    }
    return jsonify(data)
