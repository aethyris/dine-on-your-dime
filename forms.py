from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, FloatField, TextAreaField, SelectField, \
    IntegerField
from wtforms.validators import DataRequired, ValidationError, Email, EqualTo, Length, URL, InputRequired
from models import User
from flask_uploads import UploadSet, IMAGES
from flask_wtf.file import FileField, FileRequired
from flask_uploads import UploadSet, IMAGES

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Login')

class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(max=64)])
    email = StringField('Email', validators=[DataRequired(), Email(), Length(max=120)])
    password = PasswordField('Password', validators=[DataRequired()])
    password2 = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Register')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError('Please use a different username.')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError('Please use a different email address.')


class UserInfoForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(max=64)])
    email = StringField('Email', validators=[DataRequired(), Email(), Length(max=120)])
    description = TextAreaField('Description', validators=[DataRequired(), Length(max=500)])
    avatar = StringField('Avatar URL', validators=[DataRequired(), URL(), Length(max=255)])
    submit = SubmitField('Save changes')


class FilterForm(FlaskForm):
    price_min = FloatField('Price Min', validators=[InputRequired()], default=0)
    price_max = FloatField('Price Max', validators=[InputRequired()], default=100)
    meal_type = SelectField('Meal Type', choices=[('All', 'All'), ('Breakfast', 'Breakfast'), ('Lunch', 'Lunch'),
                                                  ('Dinner', 'Dinner')], default="All")
    meal_style = SelectField('Meal Style',
                             choices=[('All', 'All'), ('Fried', 'Fried'), ('BBQ', 'BBQ'), ('Steamed', 'Steamed'),
                                      ('Baked', 'Baked')], default="All")
    dietary_preferences = SelectField('Dietary Preferences', choices=[('Standard', 'Standard'), ('Vegan', 'Vegan'),
                                                                      ('Pescatarian', 'Pescatarian'),
                                                                      ('Vegetarian', 'Vegetarian')], default="Standard")
    cooking_time_min = IntegerField('Cooking Time Min', validators=[InputRequired()], default=0)
    cooking_time_max = IntegerField('Cooking Time Max', validators=[InputRequired()], default=0)
    calorie_min = IntegerField('Calorie Min', validators=[InputRequired()], default=0)
    calorie_max = IntegerField('Calorie Max', validators=[InputRequired()], default=0)
    submit = SubmitField('Save preferences')


images = UploadSet('images', IMAGES)

class photoForm(FlaskForm):
    photo = FileField(validators = [FileRequired()])
    submit = SubmitField('Upload photo')

class CommentForm(FlaskForm):
    comment = TextAreaField('Comment', validators=[DataRequired(), Length(max=800)])
    submit = SubmitField('Submit comment')
