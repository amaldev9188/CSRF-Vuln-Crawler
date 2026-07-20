import sys
from bs4 import BeautifulSoup
import requests 
url=input("Enter the URL to crawl: ")
if not url:
        print("No URL provided. Exiting.")
        exit()
response = requests.get(url)    
soup = BeautifulSoup(response.text, 'html.parser')   
forms=soup.find_all('form')
if not forms:
    print("No forms found on the page.")
    exit()
for form in forms:
    token=False
    for input in form.find_all('input',type='hidden'):
        name=input.get('name','').lower()
        if name in ['csrf_token','csrfmiddlewaretoken','authenticity_token']:
            token=True
            break
    if not token:
        print("Form without CSRF token found:")
        print("csrf vulnerability detected")
        
    else:
        print("Form with CSRF token found:")
        print("csrf protection detected")
    