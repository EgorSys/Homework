from urllib import request
from lxml import html
import json

def get_n_links(n, URL):
    link_arr = [URL]
    k = 0
    while n > 0:
        if link_arr[k].startswith('https:'):
            url = link_arr[0]
        else:
            url = 'https://en.wikipedia.org'+link_arr[k]
        page_html = request.urlopen(url).read()
        parsed_page = html.fromstring(page_html)

        for div_element in parsed_page.xpath("//a"):
            new_link = div_element.get("href")
            if not (str(new_link)[0] == '#' or new_link == None):
                link_arr.append(div_element.get("href"))
                n -= 1
            if n <= 0:
                break
        k += 1
    link_arr.pop(0)
    json.dump(link_arr, open("HW3_Web_output.txt", "w"))

get_n_links(1000, 'https://en.wikipedia.org/wiki/Small')