from flask import Flask, render_template, redirect
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length
from flask_bootstrap import Bootstrap



class myForm(FlaskForm):
    email = StringField(label='email', validators=[DataRequired(), Email(message="Invalid email address")])
    password = PasswordField(label='password', validators=[DataRequired(), Length(min=4, message="Field must be at "
                                                                                                 "least 4 characters "
                                                                                                 "long")])
    submit = SubmitField(label="Log in")

def create_app():
    app = Flask(__name__)
    Bootstrap(app)
    app.secret_key = "Hello World"
    return app

app = create_app()

@app.route("/")
def home():
    form = myForm()
    return render_template('index.html', form=form)

@app.route("/login", methods=["GET", "POST"])
def login():
    form = myForm()
    if form.validate_on_submit():
        if form.email.data == "admin@email.com" and form.password.data == "12345678":
            print(form.email.data)
            return redirect("/success")
        else:
            return redirect('/denied')
    return render_template('login.html', form=form)

@app.route("/success")
def success():
    return render_template('success.html')

@app.route("/denied")
def denied():
    return render_template('denied.html')




if __name__ == '__main__':
    app.run(debug=True)