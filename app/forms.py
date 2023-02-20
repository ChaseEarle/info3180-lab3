# Imports
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField
from wtforms.validators import DataRequired, Email

# Contact Class
class ContactForm(FlaskForm):
    """
    It represents your form using the various field types and validators available to you
    in Flask-WTF.
    """

    name = StringField('Name', validators=[DataRequired()], description="Please enter your full name.")
    email = StringField('E-mail', validators=[DataRequired(), Email()], description="Please enter your email address.")
    subject = StringField('Subject', validators=[DataRequired()], description="Please enter the subject of your message.")
    text_area = TextAreaField('Message', validators=[DataRequired()], description="Please enter the messgae you would like to send.")