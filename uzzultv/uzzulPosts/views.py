from django.shortcuts import render
from bs4 import BeautifulSoup
import requests
import random

# Create your views here.

def index(request):
  x = random.randint(1, 20000000)
  # 크롤링 할 웹 주소
  url = f'https://www.coupang.com/np/categories/178255?listSize=60&brand=&offerCondition=&filterType=&isPriceRange=false&minPrice={x}&maxPrice=2147483647&page=1&channel=user&fromComponent=N&selectedPlpKeepFilter=&sorter=salePriceAsc&filter=&rating=0'
  headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36'}

  # pip install requests 를 사용한다.
  req = requests.get(url, headers=headers)

  # 전체 페이지 html 가지고 오기
  soup = BeautifulSoup(req.text, 'html.parser')
  name = soup.select_one(".name").text.strip()  
  price = soup.select_one(".price-value").text.strip()
  src = soup.select_one('.image img')['src'].strip()
  

  return render(request, 'uzzulPosts/uzzultv.html', {'name':name,'price':price, 'src':src})
