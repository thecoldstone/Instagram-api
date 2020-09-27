from selenium.webdriver import Safari, Chrome, Firefox, ChromeOptions
import time
from requests import get
import os


class SeleniumCrawler(object):
    
    def __init__(self, usr, browser=None, headless=False):

        self.BASE_URL = "https://www.instagram.com/"

        if browser == "safari":

            # TODO
            # Not optimized yet
            self.browser = Safari()

        elif browser == "firefox":

            # TODO
            # Not optimized yet
            self.browser = Firefox()

        else:  # Chrome

            if not os.path.exists("path_chromedriver.txt"):
                raise IOError("Path to chromedriver is missing.")

            # Your path to chromedriver
            with open("path_chromedriver.txt", "r") as f:
                path_chromedriver = f.readline()

            f.close()

            # Open in headless mode
            if headless is True:

                self.op = ChromeOptions()
                self.op.add_argument('headless')

                self.browser = Chrome(executable_path=path_chromedriver, options=self.op)

            else:

                self.browser = Chrome(executable_path=path_chromedriver)

        self.browser.get(self.BASE_URL + usr)
        self.status = get(self.BASE_URL + usr).status_code
        self.logged_in = False

    def log_in(self, usr, pwd):

        from selenium.common.exceptions import NoSuchElementException

        self.browser.get(self.BASE_URL + 'accounts/login/')

        time.sleep(2)

        try:

            # Enter username
            self.browser.find_element_by_name('username').send_keys(usr)
            # Enter password
            self.browser.find_element_by_name('password').send_keys(pwd)
            # Submit form
            self.browser.find_element_by_tag_name('form').submit()

        except NoSuchElementException:

            return False, {
                'response': 'Unable to locate element to log in.'
            }

        time.sleep(2)

        success = self.browser.find_elements_by_xpath('//*[@id="slfErrorAlert"]')

        if len(success) is 0:

            time.sleep(2)

            self.browser.get(self.BASE_URL + usr)

            return True, 'Success'

        else:

            return False,  {
                'response': self.browser.find_element_by_xpath('//*[@id="slfErrorAlert"]').text
            }

    def get_posts(self):

        if self.logged_in:
            xpath_posts = '//*[@id="react-root"]/section/main/div/header/section/ul/li[1]/span'

        else:
            xpath_posts = '//*[@id="react-root"]/section/main/div/header/section/ul/li[1]/a/span'

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

    def get_all_posts(self, limit):
        '''

        :param limit: limit of posts to fetch
        :return: list of the links to the posts
        '''
        from selenium.webdriver.common.keys import Keys
        from selenium.common.exceptions import NoSuchElementException

        try:
            if self.browser.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/article/div/div/h2').text == "This Account is Private":
                return 'This Account is Private'
        except NoSuchElementException:
            pass

        time.sleep(2)

        html = self.browser.find_element_by_tag_name('html')

        posts = []

        while len(posts) < limit:

            links = [a.get_attribute('href') for a in self.browser.find_elements_by_tag_name('a')]

            try:
                # Return already gotten posts once the pop window appears that asks for logging in order to continue
                if self.browser.find_element_by_xpath('/html/body/div[5]/div[1]'):
                    return posts

            except NoSuchElementException:
                pass

            for link in links:

                if 'https://www.instagram.com/p/' in link and link not in posts:

                    if len(posts) >= limit:
                        break

                    posts.append(link)

            # Scroll down html page to load content and get more posts
            html.send_keys(Keys.END)

            time.sleep(0.5)

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

            scroll_down = "window.scrollTo(0, document.body.scrollHeight);"
            self.browser.execute_script(scroll_down)
            time.sleep(10)

        return post_likes

    def quit(self):
        self.browser.quit()
