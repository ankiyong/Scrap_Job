from django.shortcuts import render
from indeed import *



# Create your views here.
def index(request):
    return render(request,'Job_search/index.html')

def search_page(request):
    word = request.GET.get('job_name','')
    jobs = get_jobs(word)
    return render(request,'Job_search/searchpage.html',{'job':jobs,'word':word})