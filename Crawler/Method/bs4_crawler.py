from bs4 import BeautifulSoup as BS
import requests
from json import loads


class BS4(object):

    def __init__(self, usr):

        self.source, self.status = self.fetch_page(f"https://www.instagram.com/{usr}")

    @staticmethod
    def __request_url(url):

        try:
            response = requests.get(url)
        except requests.HTTPError:
            raise requests.HTTPError('Received non 200 status code from Instagram')
        except requests.RequestException:
            raise requests.RequestException
        else:
            return response

    def fetch_page(self, url):

        try:
            response = self.__request_url(url)
        except Exception as e:
            raise e
        else:
            return BS(response.text, 'html.parser'), response.status_code

    def fetch_data(self):

        scripts = self.source.find_all('script')

        data_scripts = scripts[4]

        content = data_scripts.contents[0]
        data_object = content[content.find('{"config"'):-1]
        data_json = loads(data_object)
        data_json = data_json['entry_data']['ProfilePage'][0]['graphql']['user']

        return {
            'biography': data_json['biography'],
            'followers': data_json['edge_followed_by']['count'],
            'following': data_json['edge_follow']['count'],
            'posts': data_json['edge_owner_to_timeline_media']['count']
        }
