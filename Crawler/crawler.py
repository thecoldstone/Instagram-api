class Crawler:

    def __init__(self, crawler_method):
        '''
        :param crawler_method - method which app will crawl data 
        '''

        if crawler_method is 'bs4':
            self.crawler_method = crawler_method

        elif crawler_method is 'selenium':
            self.crawler_method = crawler_method

        else:
            self.crawler_method = None
    
    def crawl(self, usr):
        '''
        :param usr - username to crawl
        '''

        if self.crawler_method is 'bs4':
            return self.crawl_with_bs4(usr)

        if self.crawler_method is 'selenium':
            return self.crawl_with_selenium(usr)

        def crawl_with_bs4(usr):
            pass

    def crawl_with_bs4(self, usr):
        '''

        :param usr: username to crawl
        :return:
        '''
        from Crawler.Method.bs4_crawler import crawl
        pass

    def crawl_with_selenium(self, usr, to_login=False):
        '''

        :param usr: username to crawl
        :return: dictionary with user's information
        '''

        # Import needed Selenium class
        from Crawler.Method.selenium_crawler import SeleniumCrawler

        selenium = SeleniumCrawler(usr)

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
            'biography': selenium.get_account_biography()
            # 'post' : selenium.get_all_posts()
        }, 'Successful'
