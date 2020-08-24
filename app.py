from flask import Flask, jsonify
from fetch import fetch_user

app = Flask(__name__)

@app.route('/user/<string:username>')
def index(username):
    result = fetch_user(username) 
    return jsonify({
        'response' : {
            'username' : result.username,
            'posts' : result.posts,
            'followers' : result.followers,
            'following' : result.following,
            'biography' : result.biography
        }

    }), 200

if __name__ == "__main__": 
    app.run(debug=True)