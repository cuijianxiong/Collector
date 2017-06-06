# -*- coding: UTF-8 -*-
from random import Random
import requests

chars1 = 'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz123456789'
chars2 = 'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz'


def random_str(randomlength=6, datas=1):

    url = ''
    chars1 = 'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz123456789'
    chars2 = 'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz'
    if datas == 1:
        chars = chars1
    if datas == 2:
        chars = chars2
    length = len(chars) - 1
    random = Random()
    for i in range(randomlength):
        url += chars[random.randint(0, length)]
    return url


def get_short_url(a,rad):
    head = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 UBrowser/6.1.2107.204 Safari/537.36"}
    url = a+'/'+rad
    response = requests.get(url=url, headers=head, allow_redirects=False)
    response.encoding = response.apparent_encoding
    if response.status_code == 302:
        reurl = response.headers.get('Location')
        print(reurl)
        return reurl
    else:
        print(url+"   >>> is false")
        return None


def scan_shortname(url, datas, number, counts):
    short_name = set()
    if url.startswith('http://'):
        url = url
    else:
        url = 'http://' + url
    urllist = set()
    for i in range(counts):
        short_name.add(random_str(randomlength=number, datas=datas))
    for rad in short_name:
        reurl = get_short_url(a=url, rad=rad)
        if reurl is not None:
            urllist.add(reurl)



def main():
    try:
        print('\033[97m')
        url = input('Please enter the domain name \n')
        datas = int(input('1 Letters + numbers \n2 Letters\n'))
        number = int(input('Letters number (better 3-6)\n'))
        counts = int(input('count number (1000-100000)\n'))
        print('\033[92m')
        scan_shortname(url=url, datas=datas, number=number, counts=counts)
    except Exception as e:
        print(e)
        print('it seems to have made a mistake')


