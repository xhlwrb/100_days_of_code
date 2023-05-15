from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import sqlite3

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///library.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy()
db.init_app(app)


class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    author = db.Column(db.String(250), nullable=False)
    rating = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return f"<Book {self.title}>"


with app.app_context():
    db.create_all()


@app.route('/')
def home():
    with app.app_context():
        all_books = db.session.execute(db.select(Book)).scalars().all()
    return render_template("index.html", list_of_books=all_books)


@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "POST":
        new_book = Book(title=request.form["title"],
                        author=request.form["author"],
                        rating=request.form["rating"])
        with app.app_context():
            db.session.add(new_book)
            db.session.commit()
        return redirect(url_for("home"))
    else:
        return render_template("add.html")


@app.route("/edit", methods=["GET", "POST"])
def edit():
    if request.method == "POST":
        book_id = request.form["id"]
        with app.app_context():
            book_to_update = db.session.execute(db.select(Book).filter_by(id=book_id)).scalar_one()
            book_to_update.rating = request.form["rating"]
            db.session.commit()
            return redirect(url_for('home'))
    book_id = request.args.get("id")
    with app.app_context():
        book_to_edit = db.session.execute(db.select(Book).filter_by(id=book_id)).scalar_one()
    return render_template("edit.html", book_to_edit=book_to_edit)


if __name__ == "__main__":
    app.run(debug=True, use_reloader=False)

