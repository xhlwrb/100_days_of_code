from flask import Flask, render_template, redirect, url_for, flash, request, abort
from flask_bootstrap import Bootstrap
from flask_ckeditor import CKEditor
from datetime import date
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user
from forms import CreatePostForm, RegisterForm, LoginForm, CommentForm
from flask_gravatar import Gravatar
from functools import wraps
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get("SECRET_KEY")
ckeditor = CKEditor(app)
Bootstrap(app)

# CONNECT TO DB
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get("DATABASE_URL",  "sqlite:///blog.db")
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
login_manager = LoginManager()
login_manager.init_app(app)

gravatar = Gravatar(app,
                    size=100,
                    rating='g',
                    default='retro',
                    force_default=False,
                    force_lower=False,
                    use_ssl=False,
                    base_url=None)

# CONFIGURE TABLES


class User(UserMixin, db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))
    posts = relationship("BlogPost", back_populates="author")
    comments = relationship("Comment", back_populates="comment_author")


class BlogPost(db.Model):
    __tablename__ = "blog_posts"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    subtitle = db.Column(db.String(250), nullable=False)
    date = db.Column(db.String(250), nullable=False)
    body = db.Column(db.Text, nullable=False)
    img_url = db.Column(db.String(250), nullable=False)
    author_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    author = relationship("User", back_populates="posts")
    comments = relationship("Comment", back_populates="comment_post")


class Comment(db.Model):
    __tablename__ = "comments"
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.Text, nullable=False)
    author_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    comment_author = relationship("User", back_populates="comments")
    post_id = db.Column(db.Integer, db.ForeignKey("blog_posts.id"))
    comment_post = relationship("BlogPost", back_populates="comments")


with app.app_context():
    # # add admin
    # admin = User()
    # admin.email = "admin@admin.com"
    # admin.password = "admin"
    # admin.name = "admin"
    # db.session.add(admin)
    # db.session.commit()
    # # add post
    # new_post = BlogPost(author_id=1,
    #                     title="some title",
    #                     subtitle="some subtitle",
    #                     date="today",
    #                     body="some body",
    #                     img_url="https://marketplace.canva.com/EAFJVhDBObw/1/0/1600w/canva-blue-and-yellow-floral"
    #                             "-pattern-desktop-wallpaper-JtylQxwr420.jpg")
    # db.session.add(new_post)
    # db.session.commit()
    # # add another user
    # new_user = User()
    # new_user.email = "xhlwrb@hotmail.com"
    # new_user.password = "123456"
    # new_user.name = "wrb"
    # db.session.add(new_user)
    # db.session.commit()
    db.create_all()

# with app.app_context():
#     new_user = User(email="xhlwrb@hotmail.com",
#                     password="123456",
#                     name="wrb")
#     db.session.add(new_user)
#     db.session.commit()
#     new_post = BlogPost(author_id=1,
#                         title="some title",
#                         subtitle="some subtitle",
#                         date="today",
#                         body="some body",
#                         img_url='https://marketplace.canva.com/EAFJVhDBObw/1/0/1600w/canva-blue-and-yellow-floral'
#                                 '-pattern-desktop-wallpaper-JtylQxwr420.jpg')
#     db.session.add(new_post)
#     db.session.commit()


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)


@app.route('/')
def get_all_posts():
    posts = BlogPost.query.all()
    return render_template("index.html", all_posts=posts)


@app.route('/register', methods=["GET", "POST"])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        with app.app_context():
            if User.query.filter_by(email=request.form.get('email')).first():
                flash("You've already signed up with that email, log in instead!")
                return redirect(url_for('login'))

            new_user = User()
            new_user.name = request.form["name"]
            new_user.email = request.form["email"]
            new_user.password = generate_password_hash(password=request.form["password"],
                                                       method='pbkdf2:sha256',
                                                       salt_length=8)
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user)
            return redirect(url_for('get_all_posts'))
    else:
        return render_template("register.html", form=form)


@app.route('/login', methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=request.form["email"]).first()
        if not user:
            flash('The email does not exist, please try again.')
            return redirect(url_for('login'))
        elif not check_password_hash(user.password, request.form["password"]):
            flash('Password incorrect. Please try again.')
            return redirect(url_for('login'))
        else:
            login_user(user)
            return redirect(url_for('get_all_posts'))
    return render_template("login.html", form=form)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('get_all_posts'))


@app.route("/post/<int:post_id>", methods=["GET", "POST"])
def show_post(post_id):
    print("inside show post")
    form = CommentForm()
    requested_post = BlogPost.query.filter_by(id=post_id).first()
    print(requested_post.body)
    if form.validate_on_submit():
        print("hi")
        try:
            new_comment = Comment(text=form.comment.data,
                                  author_id=current_user.id,
                                  post_id=post_id)
        except AttributeError:
            print("hahaha")
            flash('Sorry, only logged-in user can make a comment.')
            return redirect(url_for('login'))
        else:
            with app.app_context():
                db.session.add(new_comment)
                db.session.commit()
            return render_template("post.html", post=requested_post, form=form)
    print("h")
    return render_template("post.html", post=requested_post, form=form)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


def admin_only(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if current_user.get_id() and int(current_user.get_id()) == 1:
            return f(*args, **kwargs)
        else:
            print("404")
            return abort(404)
    return decorated_function


@app.route("/new-post", methods=["GET", "POST"])
@admin_only
def add_new_post():
    form = CreatePostForm()
    if form.validate_on_submit():
        new_post = BlogPost(
            title=form.title.data,
            subtitle=form.subtitle.data,
            body=form.body.data,
            img_url=form.img_url.data,
            author_id=current_user.id,
            date=date.today().strftime("%B %d, %Y")
        )
        db.session.add(new_post)
        db.session.commit()
        return redirect(url_for("get_all_posts"))
    return render_template("make-post.html", form=form)


@app.route("/edit-post/<int:post_id>")
@admin_only
def edit_post(post_id):
    post = BlogPost.query.get(post_id)
    edit_form = CreatePostForm(
        title=post.title,
        subtitle=post.subtitle,
        img_url=post.img_url,
        author=post.author,
        body=post.body
    )
    if edit_form.validate_on_submit():
        post.title = edit_form.title.data
        post.subtitle = edit_form.subtitle.data
        post.img_url = edit_form.img_url.data
        post.author = edit_form.author.data
        post.body = edit_form.body.data
        db.session.commit()
        return redirect(url_for("show_post", post_id=post.id))

    return render_template("make-post.html", form=edit_form)


@app.route("/delete/<int:post_id>")
@admin_only
def delete_post(post_id):
    post_to_delete = BlogPost.query.get(post_id)
    db.session.delete(post_to_delete)
    db.session.commit()
    return redirect(url_for('get_all_posts'))


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
