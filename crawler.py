from selenium.webdriver import Safari, Chrome, ChromeOptions
import time
from bs4 import BeautifulSoup
import re

BASE_URL = "https://www.instagram.com/"
EMAIL_ID = "nickita.180@yandex.ru"
EXPECTED_COLOR = "rgba(222, 20, 33, 1)"

class BrowserstackCrawler(object):
    
    def __init__(self, account, safari=False, firefox=False):
        if safari:
            self.browser = Safari()
        else:
            # Open in headless mode
            self.op = ChromeOptions()
            self.op.add_argument('headless')
            self.browser = Chrome(executable_path='/Users/macbook/chromedriver', options=self.op)
        
        self.browser.get(BASE_URL + account)

    def find_signup_btn(self):

        soap = BeautifulSoup(self.browser.page_source, 'html.parser')
        btns = soap.find_all(id=re.compile("([s|S][i|I][g|G][n|N][u|U][p|P])"))
        print(btns[0])
        # print(re.match(r'(id=\"(.*)*\")', btns[0]))

    def signup(self):
        # Confirm coockies
        coockie_cta = self.browser.find_element_by_id('accept-cookie-notification')
        coockie_cta.click()

        # Navigate to Signup Page
        button = self.browser.find_element_by_id('signupModalButton')
        button.click()

        # Fill user's full name
        username = self.browser.find_element_by_id('user_full_name')
        self.slow_typing(username, "Nikita Hohoho")
        # Fill user's email
        email = self.browser.find_element_by_id('user_email_login')
        self.slow_typing(email, EMAIL_ID)
        # Fill user's password
        password = self.browser.find_element_by_id('user_password')
        self.slow_typing(password, 'fucku') 
        # Click on Terms and Condition
        tac = self.browser.find_element_by_name('terms_and_conditions')
        tac.click()

        signupbtn = self.browser.find_element_by_id('user_submit')
        signupbtn.click()

    def slow_typing(self, element, text):
        for c in text:
            element.send_keys(c)
            time.sleep(0.2)

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

