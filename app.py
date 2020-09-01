from flask import Flask, jsonify, request
from Crawler.api import API

app = Flask(__name__)


@app.route('/')
def index():

    # Query string filled with parameters
    args = request.args

    # Initialize API
    api = API()

    respond = api.parse(args)

    if respond:
        return jsonify({
            'response': {
                'error': respond
            }
        }), 404

    result, respond = api.fetch()

    if respond:

        return jsonify({
            'response': {
                'error': respond
                }
        }), 404

    # Return json format
    return jsonify({
        'response': {
            'object': {
                'method': result['method'],
                'username': result['username'],
                'posts': result['posts'],
                'followers': result['followers'],
                'following': result['following'],
                'biography': result['biography'],
                'post': result['post']
            }
        }
    }), 200


if __name__ == "__main__":

    app.run(debug=True)
