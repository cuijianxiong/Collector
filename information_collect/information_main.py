import requests
from bs4 import BeautifulSoup
import re
import json
from .bugbank import get_Subdomain


def getdns(domain):
    url = 'https://www.virustotal.com/vtapi/v2/domain/report'
    parameters = {'domain': domain, 'apikey': '0e5c4feffd4f79dfcc85df0f504c7008985760599cad035e9c6e19d0d72dbcb3'}
    url_domain = []
    try:
        response = requests.get(url=url, params=parameters)
        response_dict = json.loads(response.text)
        for i in response_dict['subdomains']:
            url_domain.append(i)
        print(domain+'>>>>>>> is ok')
    except Exception as e:
        print(e)
        print(domain + '>>>>>>> is false')
    print(url_domain)
    return url_domain


def get_record(domain):
    url = "http://icp.chinaz.com/"+domain
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 UBrowser/6.0.1471.914 Safari/537.36'}
    response = requests.get(url=url,headers=headers)
    response.encoding = response.apparent_encoding
    response = BeautifulSoup(response.text, "lxml")
    ul = response.find('tbody', {'id': 'result_table'}).findAll('tr')
    web_data = {}
    for i in ul:
        name = i.findAll('td')[1].get_text()
        addrs = re.split(' ', i.findAll('td')[2].get_text())
        if type(addrs) == list:
            for i in range(len(addrs)):
                print(addrs[i])
                addrs[i] = addrs[i].replace('www.', '')
        else :
            addrs = addrs.replace('www.', '')
        print('网站名称： '+name+'   '+str(addrs))
        web_data[name] = addrs
    print(domain)
    web_data['domain'] = domain
    return web_data


def main():
    domain = input("Please enter the domain name \n")
    web_data = get_record(domain)
    domain_data = {}
    if web_data is not None:
        goto = input('\033[97m'+'Check for other domain names. Do you want to check subdomain? y/n\n')
        if goto is not 'n':
            goto = input(' 1 use bugbank (quick and more) \n 2 use scripts (The speed is slow)\n 3 use virustotal (number less) \n')
            goto = int(goto)
            print('\033[92m')
            print(web_data)
            if goto == 1:
                print('start use bugbank.......')
                for values in web_data.values():
                    if type(values) is list:
                        for addrs in values:
                            domain = get_Subdomain(addrs)
                            if domain is not []:
                                domain_data[addrs] = domain
                    else:
                        domain = get_Subdomain(domain=values)
                        domain_data[values] = domain
            if goto == 3:
                print('start use virustotal.......')
                for values in web_data.values():
                    if type(values) is list:
                        for addrs in values:
                            domain = getdns(domain=addrs)
                            if domain is not []:
                                domain_data[addrs] = domain
                    else:
                        domain = getdns(domain=values)
                        domain_data[addrs] = domain
            if goto == 2:
                print('start use scripts')
        print('\033[97m')
        print('all domain is over')
        print(domain_data)


