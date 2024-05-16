from celery import shared_task
import coloredlogs
import requests
from bs4 import BeautifulSoup

from estate.models import Estate

coloredlogs.auto_install()


@shared_task()
def get_estates_task():
    coloredlogs.logging.critical("Task started")

    html = requests.get("https://www.olx.uz/nedvizhimost/").text
    soup = BeautifulSoup(html, "html.parser")

    posts = soup.find_all(attrs={"class": "css-1venxj6"})
    for post in posts:
        title: str = post.find("h6").text
        price: str = (
            post.find(attrs={"data-testid": "ad-price"})
            .text.replace("Договорная", "")
            .replace("сум", "")
            .strip()
            .replace(" ", "")
        )
        location: str = (
            post.find(attrs={"data-testid": "location-date"})
            .text.split(" - ")[0]
            .strip()
        )
        area: str = (
            post.find(attrs={"class": "css-1kfqt7f"}).text.replace("м²", "").strip()
        )

        obj, created = Estate.objects.get_or_create(
            title=title, price=price, location=location, area=area
        )

        obj.save()

    coloredlogs.logging.critical("Task ended!")
