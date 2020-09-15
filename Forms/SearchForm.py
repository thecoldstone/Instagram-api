from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField, SelectField, BooleanField
from wtforms.validators import DataRequired, NumberRange, required


class SearchForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(message="Please enter username")])

    method = SelectField(u'Method', choices=[
        ('selenium', 'Selenium'),
        ('bs4', 'BeautifulSoap')])

    limit = IntegerField('Limit of posts', validators=[DataRequired(message="Please enter limit"), NumberRange(min=0, message="Integer value")])

    headless = BooleanField('Headless')
    submit = SubmitField('Fetch')
