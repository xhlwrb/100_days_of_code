from flask import Flask, render_template
import requests

app = Flask(__name__)

response = requests.get("https://api.npoint.io/6c690cba5242de857129")
response.raise_for_status()
blog_data = response.json()


@app.route('/post/<blog_id>')
def post(blog_id):
    blog_id = int(blog_id)
    return render_template("post.html", blog_i=blog_data[blog_id])


if __name__ == "__main__":
    app.run(debug=True)