from celery import shared_task
from .models import Dorama

import requests
from fake_useragent import UserAgent
from bs4 import BeautifulSoup
from django.core.files.uploadedfile import SimpleUploadedFile 
from django.core.exceptions import ObjectDoesNotExist




@shared_task
def parsing(PAGE):
    PAGE = int(PAGE)
    session = requests.Session()
    session.headers["user-agent"] = UserAgent().random
    page = 1
    while PAGE >= page:
        URL = f"https://doramy.top/page/{page}"
        page += 1

        response = session.get(URL)
            
        html_soup = BeautifulSoup(response.text, "lxml")
        items_soup = html_soup.select(".item.col-lg-2.col-sm-3.col-6 a")


        for item in items_soup:
            response = session.get(item.get("href"))
                    
            html_soup = BeautifulSoup(response.text, "lxml")
            img = html_soup.select_one(".sl_poster .img-thumbnail").get("src")
            
            name = html_soup.select_one(".sl > .sl_info.clearfix h1 span").text
            try:
                Dorama.objects.get(name=name)
            except ObjectDoesNotExist:    
                page = html_soup.select("table.table-striped.table-bordered.table-sm tr td")[-1].text
                description = html_soup.select_one(".sl_about.clearfix").text
                image = SimpleUploadedFile(name=f'{name}.jpg', 
                            content=session.get(img).content, 
                            content_type='image/jpeg') 
                Dorama.objects.create(
                    name=name,
                    description=description,
                    image=image
                )
            except Exception as e:
                continue