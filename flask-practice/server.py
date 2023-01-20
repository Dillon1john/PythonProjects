from flask import Flask, render_template
import random
import datetime
import requests
import json
app = Flask(__name__)

@app.route('/')
def home():
    random_number = random.randint(1,10)
    current_year = datetime.date.today().year
    name = "Dillon J."
    return render_template("index.html", num=random_number, year=current_year, name=name)

@app.route('/<name>')
def guess(name):

    G_response = requests.get(f"https://api.genderize.io?name={name}")
    g_json = G_response.json()
    gender = g_json["gender"]

    A_response = requests.get(f"https://api.agify.io?name={name}")
    a_json = A_response.json()
    age = a_json["age"]
    name = name.title()
    return render_template("guess.html", name=name, age=age, gender=gender)


@app.route('/blog/<num>')
def get_blog(num):
    print(num)
    blog_url = "https://api.npoint.io/c790b4d5cab58020d391"
    response = requests.get(blog_url)
    all_posts = response.json()
    return render_template("blog.html", posts=all_posts)


if __name__ == "__main__":
    app.run(debug=True)