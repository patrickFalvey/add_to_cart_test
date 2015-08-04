from django.shortcuts import render, redirect
from django.views.generic.base import RedirectView
from django.http import HttpResponse

import mechanize
from time import sleep

def home(request):
    return render(request, 'demo/index.html')

import datetime

def AddToCartDavidson(request):

    upc = '098289019349'

    

    #Instantiate mechanize browser and login to Davidson's
    br = mechanize.Browser()
    cj = mechanize.CookieJar()
    br.set_cookiejar(cj)
    br.set_handle_robots(False)
    br.addheaders = [
        ('User-agent',
         'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2062.120 Safari/537.36')
        ]
    site = "http://www11.davidsonsinc.com/Login/Login.aspx"
    br.open(site)
    br.select_form(nr=0)
    br.form['ctl00$ContentPlaceHolderNavPane$NavLoginForm$UserLogin$UserName'] = 'scott@gsadirect.com'
    br.form['ctl00$ContentPlaceHolderNavPane$NavLoginForm$UserLogin$Password'] = 'gsadirect1'
    br.submit()
'''
Choose random product page to aim the browser at using the products upc number in url.    
'''
    product_page = 'http://www11.davidsonsinc.com/Dealers/ItemDetail.aspx?sid=%s&scode=upcID' % (upc,)
    br.open(product_page)

    c_expires = datetime.datetime.now() + datetime.timedelta(days=1)
    print c_expires
    
'''
2 options for redirect below.
If redirect is pointed internally to another page in the app (/cookie/),
the cookies are passed without issue.
If the redirect is pointed to the Davidson's page,
the cookies are not present.
I am using print statements and Chrome dev-tools to observe the cookies.
'''

##    response = redirect(product_page)
    response = redirect('/cookie/')
    for cookie in cj:
        name = cookie.name
        if name != 'ASP.NET_SessionId' and name != '.ASPXAUTH':
            response.set_cookie(cookie.name, cookie.value, expires=c_expires, domain='127.0.0.1')
##            response.set_cookie(cookie.name, cookie.value, expires=c_expires, domain='www11.davidsonsinc.com/')
            print cookie.name, cookie.value, cookie.domain
        else:
            response.set_cookie(cookie.name, cookie.value, expires=c_expires,domain='127.0.0.1', httponly=True)
##            response.set_cookie(cookie.name, cookie.value, expires=c_expires,domain='www11.davidsonsinc.com/', httponly=True)
            print cookie.name, cookie.value, cookie.domain


    return response


def Cookie_Monster(request):
    cookies = request.COOKIES
    for cookie in cookies:
        print cookie
    return HttpResponse('Cookies Eaten')
