from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField, SelectField, BooleanField, PasswordField
from wtforms.validators import DataRequired, NumberRange


class SearchForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(message="Please enter username")])

    # TODO
    password = PasswordField('Password')

    method = SelectField(u'Method to crawl', choices=[
        ('selenium', 'Selenium'),
        ('bs4', 'BeautifulSoap')])

    limit = IntegerField('Limit of posts', validators=[NumberRange(min=0, message="Integer value")])

    headless = BooleanField('Headless')

    browser = SelectField(u'Browser', choices=[
        # ('safari', 'Safari'),
        ('chrome', 'Chrome')
        # ('firefox', 'Firefox')
    ])

    submit = SubmitField('Fetch')
