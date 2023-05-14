from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length
from flask_bootstrap import Bootstrap


class LoginForm(FlaskForm):
    email = StringField(label='Email', validators=[DataRequired(), Email()])
    password = PasswordField(label='Password', validators=[DataRequired(), Length(min=8)])
    submit = SubmitField(label='Log In')


app = Flask(__name__)
app.secret_key = "lalala"
bootstrap = Bootstrap(app)
email_secret = "admin@email.com"
password_secret = "12345678"


@app.route("/")
def home():
    return render_template('index.html')


@app.route('/login', methods=["GET", "POST"])
def login():
    login_form = LoginForm()
    if login_form.validate_on_submit():
        print(login_form.email.data)
        print(login_form.password.data)
        if login_form.email.data == email_secret and login_form.password.data == password_secret:
            print("yes")
            return render_template('success.html')
        else:
            print("no")
            return render_template('denied.html')
    return render_template('login.html', form=login_form)


if __name__ == '__main__':
    app.run(debug=True)