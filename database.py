# from flask_sqlalchemy import SQLAlchemy
# db = SQLAlchemy()
#
# class recipes(db.Model):
#
# __tablename__= "recipes"
#
# recipeid = db.Column(db.Integer,primary_key=True)
# title = db.Column(db.String, nullable = False)
# author = db.Column(db.String, nullable = False)
# calories = db.Column(db.String, nullable = False)
# main_ingredient = db.Column(db.String, nullable = False)
# sec_ingredient = db.Column(db.String, nullable = False)
# tert_ingredient = db.Column(db.String, nullable = False)
# vegan = db.Column(db.String, nullable = False)
# gluten_free = db.Column(db.String, nullable = False)
# vegetarian = db.Column(db.String, nullable = False)
# yield = db.Column(db.String, nullable = False)
# time = db.Column(db.String, nullable = False)
#
# class articles(db.Model):
#
# __tablename__= "artciles"
#
# articleid = db.Column(db.Integer,primary_key=True)
# author = db.Column(db.String,primary_key=True)
# title = db.Column(db.String, nullable = False)
# focus = db.Column(db.String, nullable = False)
#
# users = db.relationship("User", backref="recipes", backref="articles")
#
# def add_user(userid,fname,lname,email):
# new_user = Passenger(fname=fname, lname=lname, email=email, userid=author)
# db.session.add(new_user)
# db.session.commit()
#
# class User(db.Model):
# __tablename__ = "users"
# userid = db.Column(db.Integer, primary_key=True)
# fname = db.Column(db.String, nullable = False)
# lname = db.Column(db.String, nullable = False)
# email = db.Column(db.String, nullable = False)
#
# ingredients = db.relationship("Ingredients", backref= "recipes")
#
# def add_ingredient(id_ingredient, ingredient)
# new_ingredient = Ingredient(id_ingredient = main_ingredient, sec_ingredient, tert_ingredient, ingredient = ingredient)
# db.session.add(new_ingredient)
# db.session.commit()
#
# class Ingredient(db.Model):
# __tablename__ = "ingredients"
# id_ingredient = db.Column(db.Integer, primary_key=True)
# ingredient = db.Column(db.String, nullable=False)
