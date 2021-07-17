# Web Scrapping a real job posting website using request library and it will scrap those job posts whose requirement is python programming and had been posted a few days ago...
from bs4 import BeautifulSoup
# It requests some information from a library
import requests
import time
from PIL import Image 
import urllib.request


# html_text = requests.get('https://www.amazon.in/').text
html_text = requests.get('https://www.amazon.in/s?k=phone&ref=nb_sb_noss_2').text
soup = BeautifulSoup(html_text, 'lxml')
products = soup.find('span',class_="a-price")
print(products)
# jobs = soup.find('img', class_="landscape-image")
# print(jobs)
# urllib.request.urlretrieve( jobs['src'],
#    "pic.png")
  
# img = Image.open("pic.png")
# img.show()

