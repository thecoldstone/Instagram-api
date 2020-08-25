from selenium.webdriver import Safari, Chrome, ChromeOptions
import time
import re

BASE_URL = "https://www.instagram.com/"

class SeleniumCrawler(object):
    
    def __init__(self, usr, safari=False, firefox=False):
        if safari:
            self.browser = Safari()
        else:
            # Open in headless mode
            self.op = ChromeOptions()
            self.op.add_argument('headless')
            self.browser = Chrome(executable_path='/Users/macbook/chromedriver', options=self.op)
        
        self.browser.get(BASE_URL + usr)

    def get_posts(self):
        xpath_posts = '//*[@id="react-root"]/section/main/div/header/section/ul/li[1]/a'
        return self.browser.find_element_by_xpath(xpath_posts).text
    
    def get_followers(self):
        xpath_followers = '//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a'
        return self.browser.find_element_by_xpath(xpath_followers).text

    def get_following(self):
        xpath_following = '//*[@id="react-root"]/section/main/div/header/section/ul/li[3]/a'
        return self.browser.find_element_by_xpath(xpath_following).text
    
    def get_account_biography(self):
        xpath_biography = '//*[@id="react-root"]/section/main/div/header/section/div[2]'
        return self.browser.find_element_by_xpath(xpath_biography).text

    def get_all_posts(self):
        posts = []
        for a in self.browser.find_elements_by_tag_name('a'):
            if 'https://www.instagram.com/p/' in a.get_attribute('href'):
                posts.append(a.get_attribute('href'))
        return posts

    def get_likes(self, post):
        # Dictionary to store amount of likes for each page
        post_likes = {}
        # XPath to 'likes'
        xpath_likes = '//*[@id="react-root"]/section/main/div/div/article/div[3]/section[2]/div/div/button'
        for link in post:
            self.browser.get(link)
            post_likes[link] = self.browser.find_element_by_xpath(xpath_likes).text
            # Sleep in order to avoid an overloading of the server
            time.sleep(5)

        return post_likes    

    def quit(self):
        self.browser.quit()

