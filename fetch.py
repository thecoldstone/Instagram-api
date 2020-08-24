from crawler import BrowserstackCrawler
from user import User

def fetch_user(username):

    # Input
    user = User(username)
    # Get user's page
    bc = BrowserstackCrawler(username)
    #TODO Rewrite crawler for getting basic data. I can use Beautiful Soap for that.
    # Get basic profile's data
    user.posts = bc.get_posts()
    user.followers = bc.get_followers()
    user.following = bc.get_following()
    user.biography = bc.get_account_biography()

    bc.quit()

    return user
    