from flask_wtf import FlaskForm
from wtforms.fields import PasswordField, StringField, BooleanField, SubmitField
from wtforms.validators import DataRequired, EqualTo, ValidationError, Email
from ..models import User


class LoginForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired(), Email()])
    password = PasswordField("Password", validators=[DataRequired()])
    remember_me = BooleanField("Remember me")
    submit = SubmitField("Login")


class RegisterForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired(), Email()])
    password = PasswordField("Password", validators=[DataRequired(), EqualTo("conf_pass")])
    conf_pass = PasswordField("Confirm password", validators=[])
    submit = SubmitField("Register")

    def validate_email(self, field):
        if User.query.filter_by(email = field.data).first() is not None:
            raise ValidationError("Este email já está sendo usado.")
