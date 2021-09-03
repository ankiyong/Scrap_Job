import requests
from bs4 import BeautifulSoup
import time



def extract_info(info):
    title = info.find('h2', {'class': 'jobTitle'}).find('span', title=True).string
    company = info.find('span',{'class':'companyName'}).text
    location = info.find('div',{'class':"companyLocation"}).text
    link = 'https://kr.indeed.com'+info.parent.parent.parent.parent.parent['href']
    return {
        'title':title,
        'company': company,
        'location': location,
        'link': link
            }


def last_page(url):
    res = requests.get(url)
    soup = BeautifulSoup(res.text,'html.parser')
    max_page = soup.find('div',{'class':'pagination'}).find_all('span',{'class':'pn'})[3].text
    return max_page


def get_job(name,max_page):
    jobs = []
    for page in range(int(max_page)+1):
        url = f'https://kr.indeed.com/%EC%B7%A8%EC%97%85?as_and={name}&limit={page*50}'
        res = requests.get(url)
        soup = BeautifulSoup(res.text,'html.parser')
        result = soup.find_all('table',{'class':'jobCard_mainContent'})
        for info in result:
            job = extract_info(info)
            jobs.append(job)
    return jobs
url = 'https://kr.indeed.com/%EC%B7%A8%EC%97%85?as_and=python&limit=50'
page = last_page(url)
for i in get_job('python',page):
    print(i['title'])