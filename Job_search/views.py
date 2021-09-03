from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return render(request,'Job_search/index.html')

def search_page(request):
    return render(request,'Job_search/searchpage.html')