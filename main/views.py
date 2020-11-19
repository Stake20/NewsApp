import requests
from django.shortcuts import render
from django.http import HttpResponse
from bs4 import BeautifulSoup
from datetime import datetime
import json

url = 'https://www.timeanddate.com/weather/'

res = requests.get(url).content

soup = BeautifulSoup(res, 'html.parser')

def home(request, soup=soup):


    news_api_request = requests.get("http://newsapi.org/v2/top-headlines?country=za&apiKey=efce5d47bb684f519ff1dbbbdcaf5430")
    api = json.loads(news_api_request.content)
    date = datetime.today().date

    data = soup.find('span', class_='my-city_city')
    data1 = soup.find('span', class_='my-city_temp')
    data2 = soup.find('span', class_='my-city_desc')
    return render(request, 'home.html', {'api': api, 'city':data, 'temp':data1, 'condition':data2, 'date':date})

