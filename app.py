from flask import Flask, render_template, jsonify
from Crawler.crawler import Crawler

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("blog/index.html")

@app.route('/user/<string:username>')
def index(username):

    crawler = Crawler('selenium')

    # Whether crawl method does not exist or not yet implemented
    if crawler.crawler_method is None:
        return "<h1>Crawling method does not exist</h1>"

    # Crawl Instagram username
    result = crawler.crawl(username)

    if result is None:
        return jsonify({
            'response' : {
                'error' : 'Username is not found.'
            }
        }), 404

    # Return json format
    return jsonify({
        'response' : {
            'username' : result['username'],
            'posts' : result['posts'],
            'followers' : result['followers'],
            'following' : result['following'],
            'biography' : result['biography']
        }

    }), 200

if __name__ == "__main__": 
    app.run(debug=True)