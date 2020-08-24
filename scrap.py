from urllib.request import urlopen
from bs4 import BeautifulSoup 
import datetime
import random
import re

random.seed(datetime.datetime.now())

def get_links(articleUrl):
    html = urlopen("http://en.wikipedia.org"+articleUrl)
    bsObj = BeautifulSoup(html)

    return bsObj.find("div", {"id":"bodyContent"}).findAll("a", 
                    href=re.compile("^(/wiki/)((?!:).)*$"))

links = get_links("/wiki/Kevin_Bacon")

while len(links) > 0:
    new_article = links[random.randint(0, len(links) - 1)].attrs["href"]
    print(new_article)
    links = get_links(new_article)