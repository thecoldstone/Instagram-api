class User:
    def __init__(self, account, posts=None, followers=None, following=None):
        self.account = account
        self.posts = posts
        self.followers = followers
        self.following = following
    
    def __repr__(self):
        return {'account':self.account, 'posts':self.posts, 'followers':self.followers, 'following':self.following}

    def __str__(self):
        return 'User(account='+self.account+', posts='+str(self.posts)+', followers='+str(self.followers)+', following='+str(self.following)+ ')'
