import requests
import sys
import validators
from urllib.parse import urljoin, urlencode, urlparse, urlunparse


def valid_url(url):
    validation = validators.url(url)
    if validation:
        return True
    else: 
        return False

    
def url_creator(netloc = "something.com/", path ='gbrnvfnlewougbvf', ):
    url =  "https://" + netloc + "/" + path
    if len(url) > 256:
        print("url must be less then 256 characters")
        return 0 
    return url
    
    
#'scheme', 'netloc', 'url', 'path', 'query', 'fragment'
def shorten_link(full_link, link_name):
    API_KEY = '46db7cc2876aee6b52d44ab76e272843e36b0'
    BASE_URL = 'https://cutt.ly/api/api.php'
    
    payload = {'key': API_KEY, 'short': full_link, 'name': link_name}
    request = requests.get(BASE_URL, params = payload)
    data = request.json()
    
    print("")
    
    try:
        title = data['url']['title']
        short_link = data['url']['shortLink']
        
        print('Title:', title)
        print('Link:', short_link) 
    except:
        status = data['url']['status']
        print('Error Status:', status)
        
if __name__ == "__main__":      
    choice = int(input('''enter the option
                   creat url using function - 1
                   input it in console      - 2
                   '''))
    if choice == 1:
        link = input("Enter a link: >> ") 
        name = input("Link name for premium clients: >> ")
        tru = valid_url(link)
        if tru:
            shorten_link(link, name)
        else: sys.exit(0)

    else:
        netloc = input("input netloc....... ")
        path = input("input the path....... ")
        url = url_creator(netloc, path)
    
        name = input("Link name for premium clients: >> ")
        tru = valid_url(url)
        if tru:
            shorten_link(url, name)
        else: sys.exit(0)
    
    
