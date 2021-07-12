from flask_wtf import FlaskForm
from wtforms import StringField,FileField,IntegerField,PasswordField
from wtforms.validators import DataRequired,Length,Email

class RegistrationForm(FlaskForm):

    full_name = StringField("Full_Name",validators=[DataRequired(),Length(min=3,max=30)])
    email = StringField("Email",validators=[DataRequired(),Email()])
    address = StringField("Address",)
    image=FileField("Image",)
    age = IntegerField("Age",validators=[DataRequired(),])
    password1 = PasswordField("Password",validators= [DataRequired(),Length(min=2 ,max=30)])
    password2=PasswordField("Confirm Password",)

