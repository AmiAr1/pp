import requests
from fake_useragent import UserAgent
import os
from bs4 import BeautifulSoup


session = requests.Session()
session.headers["user-agent"] = UserAgent().random


# URL = "https://doramy.top/page/3"

# response = session.get(URL)

# with open(os.path.abspath(".html"), "w", encoding="utf-8") as f:
#     f.write(response.text)

# with open(os.path.abspath(".html"), "r", encoding="utf-8") as f:
#     html = f.read()
    
# html_soup = BeautifulSoup(html, "lxml")
# items_soup = html_soup.select(".item.col-lg-2.col-sm-3.col-6 a")

# it = 1
# for item in items_soup:
#     response = session.get(item.get("href"))
#     with open(os.path.abspath(f"{it}.html"), "w", encoding="utf-8") as f:
#         f.write(response.text) 
#     it += 1

for x in range(1, 19):
    from django.core.files.uploadedfile import SimpleUploadedFile 
    
    with open(os.path.abspath(f"{x}.html"), "r", encoding="utf-8") as f:
        html = f.read()
        
    html_soup = BeautifulSoup(html, "lxml")
    name = html_soup.select_one(".sl > .sl_info.clearfix h1 span").text
    page = html_soup.select(
        "table.table-striped.table-bordered.table-sm tr td"
    )[-1].text
    img = html_soup.select_one(".sl_poster .img-thumbnail").get("src")
    image = SimpleUploadedFile(name=f'{name}.jpg', 
                content=session.get(img).content, 
                content_type='image/jpeg') 
    
    item = {
        # "name": name,
        # "description": html_soup.select_one(".sl_about.clearfix"),
        # "series": int(page),
        "image": image
    }
    print(name)