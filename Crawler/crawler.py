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

    def crawl_with_selenium(self, usr):
        '''

        :param usr: username to crawl
        :return: dictionary with user's information
        '''

        # Import needed Selenium class
        from Crawler.Method.selenium_crawler import SeleniumCrawler

        selenium = SeleniumCrawler(usr)

        if selenium.status is not 200:
            return None

        return {
            'username': usr, 
            'posts': selenium.get_posts(),
            'followers': selenium.get_followers(),
            'following': selenium.get_following(),
            'biography': selenium.get_account_biography() 
        }
