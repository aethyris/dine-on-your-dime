from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin, AnonymousUserMixin
from datetime import datetime

db = SQLAlchemy()
followers = db.Table('followers',
    db.Column('follower_id', db.Integer, db.ForeignKey('users-table.id')),
    db.Column('followed_id', db.Integer, db.ForeignKey('users-table.id'))
)

class User(UserMixin, db.Model):
    __tablename__ = 'users-table'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), nullable=False, unique=True)
    email = db.Column(db.String(120), nullable=False, unique=True)
    password_hash = db.Column(db.String(255), nullable=False)
    description = db.Column(db.String(500), nullable=False, default="No description.")
    create_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow())
    avatar = db.Column(db.String(255), nullable=False, default="https://via.placeholder.com/200/09f/fff.png")
    filters = db.relationship('Filter', uselist=False, backref="users")
    planned_recipes = db.relationship("PlannedRecipeAssociation", back_populates="user")
    recipes = db.relationship("Recipe", uselist=False, back_populates="recipe_author")
    followed = db.relationship(
        'User', secondary=followers,
        primaryjoin=(followers.c.follower_id == id),
        secondaryjoin=(followers.c.followed_id == id),
        backref=db.backref('followers', lazy='dynamic'), lazy='dynamic')

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def follow(self, user):
        if self.followed.filter(followers.c.followed_id == user.id).first() is None:
            self.followed.append(user)

    def unfollow(self, user):
        if self.followed.filter(followers.c.followed_id == user.id).first() is not None:
            self.followed.remove(user)
        
    def followed_recipes(self):
        return Recipe.query.join(followers, (followers.c.followed_id == Recipe.recipe_author_id)).filter(followers.c.follower_id == self.id).order_by(Recipe.recipe_date.desc())

class Anon(AnonymousUserMixin):
    __tablename__ = 'anon-users-table'
    filters = db.relationship('Filter', uselist=False, backref="users")


class RecipeIngredientAssociation(db.Model):
    __tablename__ = "recipe-ingredient-association"
    recipe_id = db.Column(db.Integer, db.ForeignKey("recipes-table.recipe_id"), primary_key=True)
    ingredient_id = db.Column(db.Integer, db.ForeignKey("ingredients-table.ingredient_id"), primary_key=True)
    ingredient_quantity = db.Column(db.Numeric, nullable=False)

    ingredient = db.relationship("Ingredient", back_populates="recipes")
    recipe = db.relationship("Recipe", back_populates="ingredients")


class Recipe(db.Model):
    __tablename__ = "recipes-table"
    recipe_id = db.Column(db.Integer, primary_key=True)
    recipe_title = db.Column(db.String(120), nullable=False)
    recipe_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow())
    recipe_author_id = db.Column(db.Integer, db.ForeignKey('users-table.id'))
    recipe_author = db.relationship("User", back_populates="recipes")
    recipe_description = db.Column(db.String(2000), nullable=False)
    recipe_rating = db.Column(db.Numeric, nullable=False)
    recipe_picture = db.Column(db.String(120), nullable=False)
    recipe_cooking_time = db.Column(db.Integer, nullable=False)
    recipe_calorie_count = db.Column(db.Integer, nullable=False)

    ingredients = db.relationship("RecipeIngredientAssociation", back_populates="recipe")
    planning_users = db.relationship("PlannedRecipeAssociation", back_populates="recipe")


class Ingredient(db.Model):
    __tablename__ = "ingredients-table"
    ingredient_id = db.Column(db.Integer, primary_key=True)
    ingredient_name = db.Column(db.String(120), nullable=False)
    ingredient_description = db.Column(db.String(120), nullable=False, default="No description.")
    ingredient_picture = db.Column(db.String(120), nullable=False)
    ingredient_calorie_count = db.Column(db.Integer, nullable=False)

    recipes = db.relationship("RecipeIngredientAssociation", back_populates="ingredient")


class Filter(db.Model):
    __tablename__ = 'user-filters'
    filter_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users-table.id'))
    price_min = db.Column(db.Numeric, default=0.00)
    price_max = db.Column(db.Numeric, default=100.00)
    calorie_min = db.Column(db.Integer, default=0)
    calorie_max = db.Column(db.Integer, default=2000)
    meal_type = db.Column(db.String(32), default='All')
    meal_style = db.Column(db.String(32), default='All')
    dietary_preferences = db.Column(db.String(255), default='Standard')
    cooking_time_min = db.Column(db.Integer, default=0)
    cooking_time_max = db.Column(db.Integer, default=600)


class PlannedRecipeAssociation(db.Model):
    # Association represents each recipe a user adds to their meal plan.
    __tablename__ = 'planned-recipe-assoc'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users-table.id"))
    recipe_id = db.Column(db.Integer, db.ForeignKey("recipes-table.recipe_id"))
    start = db.Column(db.String(64), nullable=False)
    end = db.Column(db.String(64), nullable=False)
    notes = db.Column(db.String(500), default="")

    user = db.relationship("User", back_populates="planned_recipes")
    recipe = db.relationship("Recipe", back_populates="planning_users")
