import requests
import json
import sys

def get_json(url):
    domain = []
    head = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 UBrowser/6.1.2107.204 Safari/537.36"}
    response = requests.get(url=url, headers=head)
    response.encoding = response.apparent_encoding
    response = response.text
    response = json.loads(response)
    for i in response['data']:
        domain.append(i['domain'])
    return domain


def get_Subdomain(domain):
    domainlist = []
    page = 1
    url = 'http://www.bugbank.cn/api/subdomain/collect?domain=' + domain + '&page='+str(page)
    head = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 UBrowser/6.1.2107.204 Safari/537.36"}
    response = requests.get(url=url, headers=head)
    response.encoding = response.apparent_encoding
    response = response.text
    response = json.loads(response)
    total = response['page']['total']
    if total%10 == 0:
        pagetotal = total//10
    elif total%10 != 0 :
        pagetotal = total//10+1
    for i in response['data']:
        domainlist.append(i['domain'])

    if pagetotal>1:
        output = sys.stdout
        for i in range(pagetotal-1):
            page += 1
            url = 'http://www.bugbank.cn/api/subdomain/collect?domain=' + domain + '&page=' + str(page)
            domainlist = domainlist+get_json(url)
            output.write('\r'+domain+'    complete percent:%.0f%%' % (i*100/(pagetotal-1)))
        output.flush()
    return domainlist


