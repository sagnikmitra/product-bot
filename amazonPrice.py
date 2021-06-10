import requests
import bs4
import pandas as pd
from PIL import Image

HEADERS = ({'User-Agent':
            'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36',
            'Accept-Language': 'en-US, en;q=0.5'})


# url = "https://www.amazon.in/HP-Pavilion-15-6-inch-5-4600H-15-ec1051AX/dp/B08CYTHY92/"
url = "https://www.amazon.in/s?k=laptop&ref=nb_sb_noss_2"
res = requests.get(url, headers=HEADERS)
soup = bs4.BeautifulSoup(res.content, features='lxml')

amount = (soup.find(class_='sg-row').get_text().replace(
    "₹", "").strip())
print(float(amount.replace(",", "")))
name = (soup.find(class_='a-size-medium').get_text().strip())
print(str(name))
# image = soup.find(id='landingImage')
# Image.open(image).show()
