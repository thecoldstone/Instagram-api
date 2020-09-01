from user import User


class Crawler:

    def __init__(self, method=None, usr=None, pwd=""):
        '''
        :param crawler_method - method which app will crawl data 
        '''
        self.method = method
        self.usr = User(usr=usr, pwd=pwd)
        self.limit = None
        self.headless = False

    @property
    def crawler_method(self):
        return self.method

    @crawler_method.setter
    def crawler_method(self, method):

        if method == 'bs4':
            self.method = method

        elif method == 'selenium':
            self.method = method

        else:
            self.method = None

    @property
    def username(self):
        return self.usr.usr

    @username.setter
    def username(self, usr):

        if len(usr) > 0:
            self.usr.usr = usr

    @property
    def password(self):
        return self.usr.pwd

    @password.setter
    def password(self, pwd):
        self.usr.pwd = pwd

    @property
    def limit_mode(self):
        return self.limit

    @limit_mode.setter
    def limit_mode(self, limit):
        try:

            self.limit = int(limit)

        except ValueError:

            self.limit = None

    @property
    def headless_mode(self):
        return self.headless

    @headless_mode.setter
    def headless_mode(self, flag):

        try:

            if int(flag) is 0 or int(flag) is 1:
                if int(flag) is 0:
                    self.headless = False
                else:
                    self.headless = True
            else:
                self.headless = None
        except ValueError:
            self.headless = None

    def crawl(self):
        '''
        :return: dictionary with user's information
        '''
        if self.crawler_method == 'bs4':
            return self.crawl_with_bs4()

        if self.crawler_method == 'selenium':
            return self.crawl_with_selenium()

    def crawl_with_bs4(self):
        '''
        :return: dictionary with user's information parsed/crawled by BeautifulSoup
        '''
        from Crawler.Method.bs4_crawler import crawl

        return None, 'Not implemented yet'

    def crawl_with_selenium(self):
        '''
        :return: dictionary with user's information parsed/crawled by Selenium
        '''

        # Import needed Selenium class
        from Crawler.Method.selenium_crawler import SeleniumCrawler

        selenium = SeleniumCrawler(self.username, headless=self.headless)

        if len(self.password) > 0:

            selenium.logged_in, response = selenium.log_in(self.username, self.password)

            if selenium.logged_in is False and len(response) > 0:
                return None, response['response']

        if selenium.status is not 200:
            return None, 'Username is not found.'

        if self.limit is None:
            self.limit = int(selenium.get_posts())

        return {
            'method': self.crawler_method,
            'username': self.username,
            'posts': selenium.get_posts(),
            'followers': selenium.get_followers(),
            'following': selenium.get_following(),
            'biography': selenium.get_account_biography(),
            'post': selenium.get_all_posts(self.limit)
        }, ''
