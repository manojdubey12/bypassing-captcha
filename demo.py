from email import header
from http import cookies
import re
from urllib import response
from bs4 import BeautifulSoup

from requests import head, request
import requests
from config import API_KEY
from twocaptcha import TwoCaptcha

solver= TwoCaptcha('10946c2ec04f490bf2bb20b2c9141734')
url= 'https://infograins.com/contact/'
sitekey='6LcXadUbAAAAACByAVgkRKr0IJaAFMj5Xe4_wvZp'
def get_cookies(url):
    response= requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')
    csrf_el = soup.select_one('[name=csrfmiddlewaretoken]')
    csrf=csrf_el['value']
    cookies= response.cookies
    return csrf, cookies

def post_page(csrf,url,cooki,result):
    payload='k={}&tkn={}'
    headers={
        'content'-'encoding: gzip'
        'Content-Type': 'application/json',
        'Refere': 'https://infograins.com/contact/'
    }
    response= request.post(url,
                          data= payload,
                          headers=headers,
                          cookies=cooki)
    soup = BeautifulSoup(response.text, 'lxml')
    el= soup.select_one()
    return el.get_text()

def solve(url,sitekey):
    try:
        result= solver.recaptcha(sitekey=sitekey, url=url)
    except:
        print("captcha not solve")
        exit()
    return result.get('code')

def main():
    csrf, cooki = get_cookies(url)
    result= solve(url,sitekey)
    data= post_page(csrf,url,cooki,result)
    print(data)

if __name__ == '__main__':
    main()


