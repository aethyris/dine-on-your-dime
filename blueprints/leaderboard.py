from flask import Blueprint, render_template
from sqlalchemy import func
from models import User, db, Recipe, likes

leaderboard = Blueprint('leaderboard', __name__, template_folder="templates")

@leaderboard.route('/leaderboard')
def show_leaderboard():
        recipes = db.session.query(Recipe, func.count(likes.c.user_id).label('total')).join(likes).group_by(Recipe).order_by('total').limit(25).all()
        return render_template('leaderboard.html', recipes=recipes)