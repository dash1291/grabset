#!/usr/bin/env python
import re
import sys

from subprocess import call
import requests
from BeautifulSoup import BeautifulSoup as bs

class Grabber:
    def __init__(self, setUrl):
        url_re = 'flickr.com/photos/(?P<ns>[^/]+)/sets/(?P<set>[^/]+)/'
        re_search = re.search(url_re, setUrl)
        self.nsid = re_search.group('ns')
        self.setid = re_search.group('set')

    def grabSet(self, target_dir):
        set_feed_url = 'http://api.flickr.com/services/feeds/photoset.gne?' 
        set_feed_url += 'set=' + self.setid + '&nsid=' + self.nsid + '&lang=en-us'
        r = requests.get(set_feed_url)
        image_list = []
        if r.status_code == 200:
            soup = bs(r.text)
            items = soup.findAll('entry')

            for item in items:
                link_element = item.find('link', {'rel': 'enclosure'})
                link_href = link_element['href']
                image_list.append(link_href)

        call(['wget','-c', '--directory-prefix=' + target_dir + self.setid + '/'] + image_list)
        return self.setid

if __name__ == '__main__':
    g = Grabber(sys.argv[1])
    g.grabSet(sys.argv[2])
