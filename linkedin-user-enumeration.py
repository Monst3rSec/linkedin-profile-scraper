import requests
from bs4 import BeautifulSoup
import urllib2
import re
from urllib import unquote
import sys


email,password="Your_mail_id","your_linkedin_password"


test_mail=sys.argv[1]

client = requests.Session()

i=0
HOMEPAGE_URL = 'https://www.linkedin.com'
LOGIN_URL = 'https://www.linkedin.com/uas/login-submit'
url='https://www.linkedin.com/sales/gmail/profile/viewByEmail/'+test_mail
url=url 
html = client.get(HOMEPAGE_URL).content
soup = BeautifulSoup(html, "html.parser")
csrf = soup.find('input', {'name': 'loginCsrfParam'}).get('value')

login_information = {
    'session_key': email,
    'session_password': password,
    'loginCsrfParam': csrf,
    'trk': 'guest_homepage-basic_sign-in-submit'
}

client.post(LOGIN_URL, data=login_information)
#	print "code"

response = client.get(url).content
r=BeautifulSoup(response , "html.parser")



for link in r.findAll('a', href=True):
	if "profileUrl" in link.get('href'):
		profile=link.get('href').split("profileUrl=")
		url=unquote(profile[1])
		i=1
		break
if i==0:
	print "There is no profile mapped into this "+test_mail+"email id"	
else:
	print "The Linkedin profile of "+test_mail+" is \n"+url
