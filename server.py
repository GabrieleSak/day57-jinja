from flask import Flask, render_template
import random
import datetime
import requests

app = Flask(__name__)


@app.route("/")
def home():
    random_number = random.randint(1, 10)
    current_year = datetime.date.today().year
    return render_template("index.html", num=random_number, year=current_year)

@app.route("/guess/<name>")
def guess(name):
    age_response = requests.get(f"https://api.agify.io?name={name}")
    age = age_response.json()["age"]
    gender_response = requests.get(f"https://api.genderize.io?name={name}")
    gender = gender_response.json()["gender"]
    return render_template("name.html", name=name, gender=gender, age=age)


@app.route("/blog/<num>")
def get_blog(num):
    print(num)
    blog_url = "https://api.npoint.io/c790b4d5cab58020d391"
    response = requests.get(blog_url)
    all_posts = response.json()
    return render_template("blog.html", posts=all_posts)


if __name__ == "__main__":
    app.run(debug=True)
