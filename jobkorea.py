from bs4 import BeautifulSoup
import requests

def last_page(url):
    res = requests.get(url)
    soup = BeautifulSoup(res.text, 'html.parser')
    max_page = soup.find('div',{'class':'tplPagination newVer wide'}).find_all('a')[-2].text
    return max_page


def get_job(item):
    info = {}
    try:
        title = item.find('a',{'class':'title dev_view'})['title']
        company = item.find('a',{'class':'name dev_view'})['title']
        location = item.find('p',{'class':'option'}).find('span',{'class':'loc long'}).text
        link = 'https://www.jobkorea.co.kr' + item.find('a',{'class':'title dev_view'})['href']
        info = {'title':title,
                'company':company,
                'location':location,
                'link':link}
    except:
        pass
    return info

def return_job(name,max_page):
    jobs = []
    for page in range(1,int(max_page)+1):
        url = f'https://www.jobkorea.co.kr/Search/?stext={name}&Page_No={page}'
        res = requests.get(url)
        soup = BeautifulSoup(res.text,'html.parser')
        box = soup.find_all('div', {'class': 'post'})
        for item in box:
            job = get_job(item)
            jobs.append(job)
    return jobs



def get_jobs(word):
    url = f'https://www.jobkorea.co.kr/Search/?stext={word}'
    page = last_page(url)
    jobs = return_job(word,page)
    return jobs

