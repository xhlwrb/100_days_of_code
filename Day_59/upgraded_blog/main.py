from flask import Flask, render_template
import requests

app = Flask(__name__, static_folder='./static')

response = requests.get(f"https://api.npoint.io/97091225f2131cd17b06")
response.raise_for_status()
blog_data = response.json()


@app.route('/')
def home():
    return render_template("index.html", blog_data=blog_data)


@app.route('/about')
def about():
    return render_template("about.html")


@app.route('/contact')
def contact():
    return render_template("contact.html")


@app.route('/post/<int:blog_id>')
def post(blog_id):
    return render_template("post.html", blog_id=blog_id, blog_i=blog_data[blog_id])


if __name__ == "__main__":
    app.run(debug=True)
