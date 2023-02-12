from bs4 import BeautifulSoup as bs
from urllib import request
import sys
import logging
import random

def fetch_and_parse(url, dst):
    f = request.urlopen(url)
    soup = bs(f, 'html.parser')
    # find link with "next page"
    next = soup.find('a', text="next page")
    # find problems
    problems = soup.select('.mw-category-group li')
    logging.warning(len(problems))
    dst.extend(problems)

    return next


def process(url):
    s = bs('<html><head><base href="https://artofproblemsolving.com/"></base></head><body><ol></ol></body></html>', 'html.parser')
    ps = []
    next = fetch_and_parse(url, ps)
    while next is not None:
        next = fetch_and_parse(s.html.head.base['href'] + next['href'], ps)
    random.shuffle(ps)
    s.body.ol.extend(ps)    
    print(s.prettify())


if __name__ == '__main__':
    process(sys.argv[1])
