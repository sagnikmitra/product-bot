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
