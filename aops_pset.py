from os import closerange
from bs4 import BeautifulSoup as bs
from urllib import request
import sys
import os.path
import logging
import re


def process(url, dst):
    logging.warning(url)
    f = request.urlopen(url)
    soup = bs(f, 'html.parser')
    title = soup.find('h1', class_='firstHeading')
    logging.warning(title)
    dst.append(title.get_text())
    # find "Problem" node 
    prob = soup.find('h2', text=re.compile('^Problem'))
    siblings = list(prob.next_siblings)
    for p in siblings:
        if p.name == 'h2' and p.get_text().lower().find('solution') >= 0:
            break
        dst.append(p)
    return

if __name__ == '__main__':
    fname = sys.argv[1]
    base = os.path.basename(fname)
    start, end = int(sys.argv[2]), int(sys.argv[3])
    assert start > 0
    assert end >= start
    all = bs(open(fname), 'html.parser').find_all('li')
    assert end <= len(all)

    dst = bs(f'<html><head><base href="https://artofproblemsolving.com"></base></head><body><h3>{base} {start}-{end}</h3><ol></ol></body></html>', 'html.parser')
    for p in all[start-1:end]:
        li = dst.new_tag('li')
        li.append(dst.new_tag('hr'))
        dst.ol.append(li)
        process(dst.base['href'] + p.a['href'], li)
    print(dst.prettify())
