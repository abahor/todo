from flask_wtf import FlaskForm
from flask_wtf.file import FileAllowed, FileField
from markupsafe import Markup
from wtforms import StringField, SubmitField, FloatField, PasswordField, TextAreaField, SelectField
from wtforms.validators import DataRequired, EqualTo, Email, InputRequired, length, ValidationError

from myproject.models import UsersModel


class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()], render_kw={'placeholder': 'Email'})
    password = PasswordField('Password', validators=[DataRequired()], render_kw={'placeholder': 'Password'})
    submit = SubmitField("Login")


def check_email(self, args):
    user = UsersModel.query.filter_by(email=self.email.data).first()
    print(self.email.data)
    if user:
        raise ValidationError((Markup('''
   This email already exist try <strong><a href="/login">login</a></strong> instead.''')))


def validate_username(self, field):
    excluded_chars = " *?!'^+%&/()=}][{$#"
    for char in self.username.data:
        if char in excluded_chars:
            raise ValidationError(
                f"Character {char} is not allowed in username.")


class adding_new(FlaskForm):
    title = StringField("title",
                        validators=[InputRequired(),],
                        render_kw={'placeholder': 'title'})
    description = TextAreaField('Description',
                                validators=[InputRequired()], render_kw={'placeholder': 'Description of the meal'})
    # price = Num('Enter the price of the item', validators=[InputRequired()], render_kw={'placeholder': 'Price'})
    # kind = SelectField(u'Type of the food',
                       # choices=[('food', 'Food'), ('soda', 'Soda'), ('juice', 'Juice'),
                                # ('coffee', 'Coffee'), ('tea', 'Tea'), ('dessert', 'Dessert')],
                       # validators=[InputRequired()])
    # preparation_time = Num("Enter the average time it take to prepare this meal in minutes",
                           # msg="Enter the time it take to prepare this meal in minutes ",
                           # validators=[InputRequired()], render_kw={'placeholder': 'Time in minutes'})
    submit = SubmitField('Add')
