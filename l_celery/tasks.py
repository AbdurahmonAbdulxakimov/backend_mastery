# feedback/tasks.py

from time import sleep
from celery import shared_task
import logging
import requests
from bs4 import BeautifulSoup

from l_celery.models import Team


@shared_task()
def get_teams_task():
    logging.info("Task started...")

    html = requests.get("https://stadion.uz/").text
    soup = BeautifulSoup(html, "html.parser")
    clubs = soup.select("#standings_place > table:nth-child(1) > tr")[1:-1]

    for club in clubs:
        name: str = club.findChildren()[4].text.strip()
        games: int = int(club.findChildren()[4].text.strip())
        score: int = int(club.findChildren()[4].text.strip())

        team, _ = Team.objects.get_or_create(title=name)
        team.games_count = games
        team.score_count = score
        team.save()

    logging.info("Task ended!")
