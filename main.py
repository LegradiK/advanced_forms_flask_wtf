from flask import Flask, render_template, flash
from flask_wtf import FlaskForm
from flask_bootstrap import Bootstrap5
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length

'''
Red underlines? Install the required packages first: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from requirements.txt for this project.
'''

class MyForm(FlaskForm):
    email = StringField(label='Email', validators=[DataRequired(), Email()])
    password = PasswordField(label='Password', validators=[DataRequired(), Length(min=8, message="Password must be at least 8 characters." )])
    submit = SubmitField(label='Log In')

app = Flask(__name__)
app.secret_key = "any-string-you-want-just-keep-it-secret"
bootstrap = Bootstrap5(app)

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/login", methods=("GET","POST"))
def login():
    myform = MyForm()
    if  myform.validate_on_submit():
        if myform.email.data == "admin@email.com" and myform.password.data == "12345678":
            return render_template('success.html') 
        else:
            return render_template('denied.html')
    return render_template('login.html', form=myform)

if __name__ == '__main__':
    app.run(debug=True)

