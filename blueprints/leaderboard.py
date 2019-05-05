from flask import Blueprint, render_template, request
from models import *

home_page = Blueprint('home_page', __name__, template_folder="templates"

from flask import Blueprintß


def leaderboard(screen, score, highscore):

    if score>=highscore:
        highscore=int(round(score,0))


if __name__ == "__main__":


    while True:
       score=10
       screen = leaderboard.display.
       leaderboard(screen,score)
       leaderboard.display.update()


       def get_count(q):
    count_q = q.statement.with_only_columns([func.count()]).order_by(None)
    count = q.session.execute(count_q).scalar()
    return count
