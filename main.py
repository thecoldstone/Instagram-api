from crawler import BrowserstackCrawler
from user import User

if __name__ == "__main__":

    # Input
    user = User(input("Enter instagram account: "))
    # Get user's page
    bc = BrowserstackCrawler(user.account)
    # Get basic profile's data
    user.posts = bc.get_posts()
    user.followers = bc.get_followers()
    user.following = bc.get_following()

    # print(user)

    # Get user's like
    # print(bc.get_likes(bc.get_all_posts()))

    bc.quit()