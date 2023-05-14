from flask import Flask, render_template, request
import requests
import smtplib

app = Flask(__name__, static_folder='./static')

response = requests.get(f"https://api.npoint.io/97091225f2131cd17b06")
response.raise_for_status()
blog_data = response.json()
my_email = "100daysg@gmail.com"
my_password = "gfjzvlmufwfzjkla"
send_email = "yh100days@yahoo.com"


@app.route('/')
def home():
    return render_template("index.html", blog_data=blog_data)


@app.route('/about')
def about():
    return render_template("about.html")


@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        with smtplib.SMTP("smtp.gmail.com", 587, timeout=120) as connection:
            connection.starttls()
            connection.login(user=my_email, password=my_password)
            connection.sendmail(from_addr=my_email,
                                to_addrs=send_email,
                                msg=f"Subject:Form Completed!\n\n"
                                    f"name: {request.form['name']}\n"
                                    f"email: {request.form['email']}\n"
                                    f"phone: {request.form['phone']}\n"
                                    f"message: {request.form['message']}")
        return render_template("contact.html", successful="Successfully sent message")
    else:
        return render_template("contact.html", successful="Contact Me")


@app.route('/post/<int:blog_id>')
def post(blog_id):
    return render_template("post.html", blog_id=blog_id, blog_i=blog_data[blog_id])


if __name__ == "__main__":
    app.run(debug=True)
