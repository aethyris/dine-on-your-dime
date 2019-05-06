from flask import Blueprint, render_template, request
from models import User, db, Recipe

leaderboard = Blueprint('leaderboard', __name__, template_folder="templates")


