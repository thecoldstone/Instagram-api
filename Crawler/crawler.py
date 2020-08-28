class Crawler:

    def __init__(self, method=None):
        '''
        :param crawler_method - method which app will crawl data 
        '''
        self.method = method

    # Getter function
    @property
    def crawler_method(self):
        return self.method

    # Setter function
    @crawler_method.setter
    def crawler_method(self, method):

        if method == 'bs4':
            self.method = method

        elif method == 'selenium':
            self.method = method

        else:
            self.method = None

    def crawl(self, usr, headless=False):
        '''
        :param usr - username to crawl
        :param headless - do not open browser
        '''

        if self.crawler_method == 'bs4':
            return self.crawl_with_bs4(usr)

        if self.crawler_method == 'selenium':
            return self.crawl_with_selenium(usr, headless)

        # def crawl_with_bs4(usr):
        #     pass

    @staticmethod
    def crawl_with_bs4(usr):
        '''
        :param usr: username to crawl
        :return:
        '''
        from Crawler.Method.bs4_crawler import crawl
        pass

    @staticmethod
    def crawl_with_selenium(usr, headless=False, to_login=False):
        '''
        :param usr: username to crawl
        :param headless: do not open browser
        :param to_login: whether user wants to log in and scrap closed account
        :return: dictionary with user's information
        '''

        # Import needed Selenium class
        from Crawler.Method.selenium_crawler import SeleniumCrawler

        selenium = SeleniumCrawler(usr, headless=headless)

        if to_login is True:

            selenium.logged_in, response = selenium.log_in('nike', 'sdad')

            if selenium.logged_in is False and len(response) > 0:
                return None, response['response']

        if selenium.status is not 200:
            return None, 'Username is not found.'

        return {
            'username': usr,
            'posts': selenium.get_posts(),
            'followers': selenium.get_followers(),
            'following': selenium.get_following(),
            'biography': selenium.get_account_biography(),
            'post' : selenium.get_all_posts()
        }, 'Successful'
