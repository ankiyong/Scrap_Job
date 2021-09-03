from django.shortcuts import render
from django.http import HttpResponse
from scrapper import *
# Create your views here.
def index(request):
    return render(request,'Job_search/index.html')

def search_page(request):
    url = 'https://kr.indeed.com/%EC%B7%A8%EC%97%85?as_and=python&limit=50'
    page = last_page(url)
    word = request.GET.get('job_name','')
    jobs = get_job('python',page)
    return render(request,'Job_search/searchpage.html',{'job':jobs,'word':word})