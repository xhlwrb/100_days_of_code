from flask import Flask, render_template
import requests

app = Flask(__name__)


@app.route('/guess/<name>')
def home(name):
    response = requests.get(f"https://api.genderize.io?name={name}")
    response.raise_for_status()
    gender_data = response.json()
    gender = gender_data["gender"]
    response = requests.get(f"https://api.agify.io?name={name}")
    response.raise_for_status()
    age_data = response.json()
    age = age_data["age"]
    return render_template("index.html", name=name.capitalize(), gender=gender, age=age)


@app.route('/blog/<num>')
def get_blog(num):
    print(num)
    blog_url = "https://api.npoint.io/6c690cba5242de857129"
    response = requests.get(blog_url)
    all_posts = response.json()
    return render_template("blog.html", posts=all_posts)

if __name__ == "__main__":
    app.run(debug=True)