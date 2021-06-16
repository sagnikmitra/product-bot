import requests
import bs4
import pandas as pd
from PIL import Image
import streamlit as st

HEADERS = ({'User-Agent':
            'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36',
            'Accept-Language': 'en-US, en;q=0.5'})


url = "https://www.amazon.in/HP-Pavilion-15-6-inch-5-4600H-15-ec1051AX/dp/B08CYTHY92/"
# url = "https://www.amazon.in/s?k=laptop&ref=nb_sb_noss_2"
res = requests.get(url, headers=HEADERS)
soup = bs4.BeautifulSoup(res.content, features='lxml')

amount = (soup.find(id='priceblock_ourprice').get_text().replace(
    "₹", "").strip())

amount = (soup.find(id='priceblock_ourprice').get_text().replace(
    "₹", "").strip())

print(float(amount.replace(",", "")))
# st.write(float(amount.replace(",", "")))
name = (soup.find(id='productTitle').get_text().strip())
print(str(name))
# st.write(str(name))
