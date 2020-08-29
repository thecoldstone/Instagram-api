class User:
    def __init__(self, **kwargs):

        for key, value in kwargs.items():
            if 'usr' is key:
                self.usr = value
            if 'pwd' is key:
                self.pwd = value

        self.posts = None
        self.followers = None
        self.following = None
        self.post = []

    def __repr__(self):
        return {'usr':self.usr, 'pwd':self.pwd, 'posts':self.posts, 'followers':self.followers, 'following':self.following}

    def __str__(self):
        return 'User(usr='+self.usr+', pwd='+self.pwd+')'
