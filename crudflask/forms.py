from flask_wtf import FlaskForm
from flask_wtf.file import FileField,FileAllowed
from wtforms.validators import Email,DataRequired,InputRequired, Length, ValidationError, EqualTo,ValidationError
from wtforms import StringField, PasswordField, SubmitField, BooleanField,EmailField,TextAreaField

from crudflask.models import User

################################################################################# Forms 
#-1------------Insert form
class InsertForm(FlaskForm):
    username = StringField('UserName:', validators=[DataRequired(), Length(min=3, max=20)])
    email = StringField('Email:',validators=[DataRequired(), Email()])
    phone = StringField('Phone:')
    submit = SubmitField('Sign Up')

    def validate_username(self,username):
        user = User.query.filter_by(username=username.data).first()   
        if user:
            raise ValidationError('UserName alredy used , pleaze choose another one')
            
        
    def validate_email(self,email):
        user = User.query.filter_by(email=email.data).first()   #email field comming from the form in parameter of register()
        if user:
            raise ValidationError('Email alredy used , pleaze choose another one')
            
#-2------------Update form
class UpdateForm(FlaskForm):
    username = StringField('UserName:', validators=[DataRequired(), Length(min=3, max=20)])
    email = StringField('Email:',validators=[DataRequired(), Email()])
    phone = StringField('Phone:')
    submit = SubmitField('Sign Up')
