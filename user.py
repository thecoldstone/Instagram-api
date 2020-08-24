class User:
    def __init__(self, username):
        self.username = username
        self.posts = None
        self.followers = None
        self.following = None
        self.biography = None
    
    def __repr__(self):
        return {'account':self.username, 'posts':self.posts, 'followers':self.followers, 'following':self.following}

    def __str__(self):
        return 'User(account='+self.username+', posts='+str(self.posts)+', followers='+str(self.followers)+', following='+str(self.following)+ ')'
