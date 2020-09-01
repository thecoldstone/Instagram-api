from flask import request
from Crawler.crawler import Crawler


class API:

    def __init__(self):

        self.crawler = Crawler()

    def parse(self, args):
        '''
        :param args: query string filled with parameters
        :return: initialized crawler
        '''

        if 'username' in args:

            self.crawler.username = request.args.get('username')

            if self.crawler.username is None:
                return {
                        'username': 'Not defined.'
                    }

        else:

            return {
                    'username': 'Not defined.'
                }

        if 'method' in args:

            self.crawler.crawler_method = request.args.get('method')

            if self.crawler.crawler_method is None:
                return {
                        'method': '{0} {1} {2}'.format('Method', request.args.get('method'), 'does not exist.')
                    }

        else:

            return {
                    'method': 'Not defined'
                }

        if 'limit' in args:

            self.crawler.limit_mode = request.args.get('limit')

            if self.crawler.limit_mode is None:
                return {
                        'limit': 'Limit is not integer type.'
                    }

        # Whether the user wants to log in and scrap his own private account
        if 'pwd' in args:
            self.crawler.password = request.args.get('pwd')

        if 'headless' in args:

            self.crawler.headless_mode = request.args.get('headless')

            if self.crawler.headless_mode is None:
                return {
                        'headless': 'Headless mode is supposed to be an integer value between 0 or 1.'
                    }

    def fetch(self):
        '''
        :return: crawled Instagram account
        '''
        result, respond = self.crawler.crawl()

        return result, respond
