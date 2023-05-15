from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FloatField
from wtforms.validators import DataRequired
import requests

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///movies.db"
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
moviedb_api_key = "964d257293dfada93e5b83a02113e46e"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy()
db.init_app(app)
Bootstrap(app)


class MovieForm(FlaskForm):
    movie_title = StringField('Movie Title', validators=[DataRequired()])
    submit = SubmitField('Add Movie')


class RateMovieForm(FlaskForm):
    rating = FloatField('Your Rating out of 10 e.g. 7.5', validators=[DataRequired()])
    review = StringField('Your Review', validators=[DataRequired()])
    submit = SubmitField('Done')


class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    year = db.Column(db.String(4), nullable=False)
    description = db.Column(db.UnicodeText, nullable=False)
    rating = db.Column(db.Float, nullable=True)
    ranking = db.Column(db.Integer, unique=True)
    review = db.Column(db.UnicodeText, nullable=True)
    img_url = db.Column(db.String(250), nullable=False)

    def __repr__(self):
        return f"<Movie {self.title}>"


with app.app_context():
    db.create_all()

# with app.app_context():
#     new_movie = Movie(
#         title="The African Queen",
#         year=1931,
#         description="A famous left-wing satirical comedy about two ex-convicts, one of whom escaped jail and then worked his way up from salesman to factory owner, where he oversees a highly mechanized operation where the workers are reduced to mere automatons. Fearful of being exposed over his past, at first by his friend and later by another gangster, the owner chooses to give his factory to the workers, then escapes with his friend to the freedom of the open road. The production company for 'A Nous la Liberte' was for more than a decade embroiled in a lawsuit claiming that Charles Chaplin had seen their film and plagiarized many ideas from it as he developed 'Modern Times.'",
#         rating=7.7,
#         ranking=1,
#         review="Seeking better life, two convicts escape from prison.",
#         img_url="https://m.media-amazon.com/images/M/MV5BYzM3YjE2NGMtODY3Zi00NTY0LWE4Y2EtMTE5YzNmM2U1NTg2XkEyXkFqcGdeQXVyMTY5Nzc4MDY@._V1_UX140_CR0,0,140,209_AL_.jpg"
#     )
#     db.session.add(new_movie)
#     db.session.commit()


@app.route("/")
def home():
    with app.app_context():
        all_movies = db.session.execute(db.select(Movie).order_by(Movie.rating)).scalars().all()
    for i in range(len(all_movies)):
        all_movies[i].ranking = len(all_movies) - i
    db.session.commit()
    return render_template("index.html", list_of_movies=all_movies)


@app.route("/edit", methods=["GET", "POST"])
def edit():
    form = RateMovieForm()
    if form.validate_on_submit():
        movie_id = request.args.get("id")
        new_rating = form.rating.data
        new_review = form.review.data
        print(movie_id)
        print(new_rating)
        with app.app_context():
            movie_to_update = db.session.execute(db.select(Movie).filter_by(id=movie_id)).scalar_one()
            movie_to_update.rating = new_rating
            movie_to_update.review = new_review
            db.session.commit()
            return redirect(url_for('home'))
    else:
        return render_template("edit.html", form=form)


@app.route("/delete")
def delete():
    movie_id = request.args.get("id")
    with app.app_context():
        movie_to_delete = db.session.execute(db.select(Movie).filter_by(id=movie_id)).scalar_one()
        db.session.delete(movie_to_delete)
        db.session.commit()
        return redirect(url_for('home'))


@app.route("/add", methods=["GET", "POST"])
def add():
    form = MovieForm()
    if form.validate_on_submit():
        query = form.movie_title.data
        print(query)
        movie_params = {
            "api_key": moviedb_api_key,
            "query": query,
        }
        response = requests.get("https://api.themoviedb.org/3/search/movie", params=movie_params)
        response.raise_for_status()
        movie_data = response.json()
        print(movie_data["results"])
        return render_template("select.html", movies_found=movie_data["results"])
    else:
        return render_template("add.html", form=form)


@app.route("/select", methods=["GET", "POST"])
def select():
    movie_id = request.args.get("id")
    movie_params = {
        "api_key": moviedb_api_key,
    }
    response = requests.get(f"https://api.themoviedb.org/3/movie/{movie_id}", params=movie_params)
    response.raise_for_status()
    movie_data = response.json()

    with app.app_context():
        new_movie = Movie(
            title=movie_data["original_title"],
            year=movie_data["release_date"][:4],
            description=movie_data["overview"],
            img_url=f"https://image.tmdb.org/t/p/w500{movie_data['poster_path']}"
        )
        db.session.add(new_movie)
        db.session.commit()

    return redirect(url_for('edit', id=new_movie.id))


if __name__ == '__main__':
    app.run(debug=True, use_reloader=False)
