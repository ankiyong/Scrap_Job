from django.shortcuts import render
from indeed import *
from jobkorea import *


# Create your views here.
def index(request):
    return render(request,'Job_search/index.html')

def search_page(request):
    word = request.GET.get('job_name','')
    site = request.GET.get('chk','')
    if site == 'indeed1':
        jobs = get_jobs(word)
    else:
        jobs = get_kor_jobs(word)
    return render(request,'Job_search/searchpage.html',{'job':jobs,'word':word})