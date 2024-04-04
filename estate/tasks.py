from celery import shared_task
import coloredlogs
import requests
from bs4 import BeautifulSoup

from estate.models import Estate


@shared_task()
def get_estates_task():
    coloredlogs.info("\nTask started...")

    html = requests.get("https://www.olx.uz/nedvizhimost/").text
    soup = BeautifulSoup(html, "html.parser")

    posts = soup.find_all(attrs={"class": "css-1venxj6"})
    for post in posts:
        title: str = post.find("h6").text
        price: float = float(
            post.find(attrs={"data-testid": "ad-price"})
            .text.replace("Договорная", "")
            .replace("сум", "")
            .strip()
        )
        location: str = (
            post.find(attrs={"data-testid": "location-date"})
            .text.split(" - ")[0]
            .strip()
        )
        area: str = post.find(attrs={"class": "css-1kfqt7f"}).text

        Estate.objects.create(title=title, price=price, location=location, area=area)

    coloredlogs.info("Task ended!")
