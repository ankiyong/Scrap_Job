import requests
from bs4 import BeautifulSoup
import time
url = 'https://kr.indeed.com/%EC%B7%A8%EC%97%85?as_and=python&limit=50'
# def extract_info(url):
res = requests.get(url)
soup = BeautifulSoup(res.text,'html.parser')
result = soup.find_all('table',{'class':'jobCard_mainContent'})
for info in result:
    title = info.find('h2', {'class': 'jobTitle'}).find('span', title=True).string
    company = info.find('span',{'class':'companyName'}).text
    location = info.find('div',{'class':"companyLocation"}).text
    link = info.parent.parent.parent.parent.parent['href']
    return {
        'title':title,
        'company':company,
        'location':location,
        'link' : link
    }


def last_page(url):
    res = requests.get(url)
    soup = BeautifulSoup(res.text,'html.parser')
    max_page = soup.find('div',{'class':'pagination'}).find_all('span',{'class':'pn'})[3].text
    return max_page
