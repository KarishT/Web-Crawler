from urllib2 import urlopen
from bs4 import BeautifulSoup, SoupStrainer

import pprint
pp = pprint.PrettyPrinter()
url = 'http://www.codingdojo.com'

def printlinks(url):
    soup = BeautifulSoup(urlopen(url), "html.parser")
    links = soup.findAll('a', href = True)
    listoflinks = []
    for link in links:
        if link not in listoflinks:
            listoflinks.append(link['href'])
    print(listoflinks)
printlinks(url)
# links = SoupStrainer('a')
# somethig =[tag for tag in BeautifulSoup(urlopen(url), parse_only=links)]
# print somethig
