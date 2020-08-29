from flask import Flask, jsonify, request
from Crawler.crawler import Crawler

app = Flask(__name__)


@app.route('/')
def index():

    args = request.args
    crawler = Crawler()

    if 'username' in args:

        crawler.username = request.args.get('username')

    else:

        return jsonify({
            'response': {
                'username': 'Not defined.'
            }
        }), 404

    if 'method' in args:

        crawler.crawler_method = request.args.get('method')

        if crawler.method is None:
            return jsonify({
                'response': {
                    'method': '{0} {1} {2}'.format('Method', request.args.get('method'), 'does not exist.')
                }
            }), 404
    else:

        return jsonify({
                'response': {
                    'method': 'Not defined'
                }
            }), 404

    # Whether crawl method does not exist or not yet implemented
    if crawler.method is None:

        return jsonify({
            'response': {
                'method': '{0} {1} {2}'.format('Method', request.args.get('method'), 'does not exist')
            }
        }), 404

    # Whether the user wants to log in and scrap his own private account
    if 'pwd' in args:

        crawler.password = request.args.get('pwd')

    # Crawl Instagram username
    result, respond = crawler.crawl(headless=True)

    if result is None:

        return jsonify({
            'response': {
                'method': request.args.get('method'),
                'error': respond
            }
        }), 404

    # Return json format
    return jsonify({
        'response': {
            'method': request.args.get('method'),
            'username': result['username'],
            'posts': result['posts'],
            'followers': result['followers'],
            'following': result['following'],
            'biography': result['biography'],
            'post': result['post']
        }

    }), 200


if __name__ == "__main__":

    app.run(debug=True)
