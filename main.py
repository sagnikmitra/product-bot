<<<<<<< HEAD
import bs4 as bs
import sys
import schedule
import time
import urllib.request
from PyQt5.QtWebEngineWidgets import QWebEnginePage
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import QUrl

import winsound
frequency = 2500  # Set Frequency To 2500 Hertz
duration = 1000  # Set Duration To 1000 ms == 1 second


class Page(QWebEnginePage):

    def __init__(self, url):
        self.app = QApplication(sys.argv)
        QWebEnginePage.__init__(self)
        self.html = ''
        self.loadFinished.connect(self._on_load_finished)
        self.load(QUrl(url))
        self.app.exec_()

    def _on_load_finished(self):
        self.html = self.toHtml(self.Callable)
        print('Load finished')

    def Callable(self, html_str):
        self.html = html_str
        self.app.quit()


def exact_url(url):
    index = url.find("B0")
    index = index + 10
    current_url = ""
    current_url = url[:index]
    return current_url


def mainprogram():
    url = "https://www.amazon.in/Airtel-4G-Hotspot-E5573Cs-609-Portable/dp/B06WV9WR4Z"
    exacturl = exact_url(url)  # main url to extract data
    page = Page(exacturl)
    soup = bs.BeautifulSoup(page.html, 'html.parser')
    js_test = soup.find('span', id='priceblock_ourprice')
    if js_test is None:
        js_test = soup.find('span', id='priceblock_dealprice')
    str = ""
    for line in js_test.stripped_strings:
        str = line

    # convert to integer
    str = str.replace(", ", "")
    current_price = int(float(str))
    your_price = 600
    if current_price < your_price:
        print("Price decreased book now")
        winsound.Beep(frequency, duration)
    else:
        print("Price is high please wait for the best deal")


def job():
    print("Tracking....")
    mainprogram()


# main code
schedule.every(1).minutes.do(job)

while True:
    schedule.run_pending()
    time.sleep(1)
=======
# Web Scrapping a real job posting website using request library and it will scrap those job posts whose requirement is python programming and had been posted a few days ago...
from bs4 import BeautifulSoup
# It requests some information from a library
import requests
import time
from PIL import Image
import urllib.request
import streamlit as st
# print("Put some skills that you are not familiar with...")
# unfamiliar_skill = input('>')
# print(f'Filtering out {unfamiliar_skill}')
# html_text = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation=')
# It returns status code
# print(html_text)
# def find_jobs():
html_text = requests.get(
    'https://www.amazon.in/s?k=phones').text
# It returns html code
# print(html_text)
soup = BeautifulSoup(html_text, 'lxml')
jobs = soup.find('img', class_="s-image")
# price = soup.find('span', class_="a-price-whole")
# print(jobs)
# print(jobs['src'])
# Image.open(jobs['src']).show()
# urllib.request.urlretrieve(jobs['src'],
#                            "pic.png")
# st.write(price)
st.image(jobs['src'])
# img = Image.open("pic.png")
# img.show()

# jobs = soup.find_all('li', class_='clearfix job-bx wht-shd-bx')
# print(job)
#     for index,job in enumerate(jobs):
#         published_date= job.find('span', class_='sim-posted').text
#         if 'few' in published_date:
#             # replace is used to remove unwanted blank spaces
#             company_name = job.find('h3',class_='joblist-comp-name').text.replace(' ','')
#             skills = job.find('span',class_="srp-skills").text.replace(' ','')
#             more_info = job.header.h2.a['href']
#             if unfamiliar_skill not in skills:
#                 with open(f'results/{index}.txt','w') as f:
#                     f.write(f'Company Name: {company_name.strip()} \n')
#                     f.write(f'Skills: {skills.strip()} \n')
#                     f.write(f'More Info: {more_info} \n')
#                 print(f'File saved: {index}.txt')
#                 # print(f'''
#                 #     Company Name: {company_name}
#                 #     Skills: {skills}
#                 # ''')

# if __name__ == '__main__':
#     while True:
#         find_jobs()
#         time_wait=10
#         print(f'Waiting {time_wait} minutes....')
#         time.sleep(time_wait*60)
>>>>>>> shivani
