from django.urls import path
from . import views
urlpatterns = [
    path('',views.index,name='index'),
    path('searchpage/',views.search_page,name='search'),
]