from flask import Flask, jsonify, request
from flask import render_template, redirect, url_for
from flask_wtf.csrf import CSRFProtect
from flask_bootstrap import Bootstrap
from Crawler.api import API
import os


def create_app():

    csrf = CSRFProtect()
    app = Flask(__name__)

    csrf.init_app(app)

    SECRET_KEY = os.urandom(32)
    app.config['SECRET_KEY'] = SECRET_KEY

    Bootstrap(app)

    return app


app = create_app()


@app.route('/welcome', methods=('GET', 'POST'))
def welcome_page():
    '''
    Simple GUI for API

    '''
    from Forms.SearchForm import SearchForm

    # Using meta to disable the appearing of csrf in url
    search = SearchForm()

    # Once form has been submitted
    if search.validate_on_submit():
        # TODO
        # We need to parse search.data in order to create a proper and meaningful query
        return search.data

    return render_template('welcome.html', form=search)


@app.route('/')
def index():
    '''
    API Module

    :return: json object
    '''

    # Query string filled with parameters
    args = request.args

    # If query string has been omitted we render welcome template
    if len(args) == 0:
        return redirect(url_for('welcome_page'))

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
                'username': result['username'],
                'posts': result['posts'],
                'followers': result['followers'],
                'following': result['following'],
                'biography': result['biography'],
                'post': result['post']
            },
            'settings': {
                'method': result['method']
            }
        }
    }), 200


if __name__ == "__main__":

    app.run()
