from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
from random import choice

app = Flask(__name__)

# Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
API_KEY = "TOPSECRET"
db = SQLAlchemy(app)


# Cafe TABLE Configuration
class Cafe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=True, nullable=False)
    map_url = db.Column(db.String(500), nullable=False)
    img_url = db.Column(db.String(500), nullable=False)
    location = db.Column(db.String(250), nullable=False)
    seats = db.Column(db.String(250), nullable=False)
    has_toilet = db.Column(db.Boolean, nullable=False)
    has_wifi = db.Column(db.Boolean, nullable=False)
    has_sockets = db.Column(db.Boolean, nullable=False)
    can_take_calls = db.Column(db.Boolean, nullable=False)
    coffee_price = db.Column(db.String(250), nullable=True)


with app.app_context():
    db.create_all()


@app.route("/")
def home():
    return render_template("index.html")


# HTTP GET - Read Record
# random cafe
@app.route("/random")
def random():
    # fetch a random cafe
    with app.app_context():
        all_cafes = db.session.execute(db.select(Cafe)).scalars().all()
        db.session.commit()
        random_cafe = choice(all_cafes)
        # convert cafe to json
        return jsonify(name=random_cafe.name,
                       map_url=random_cafe.map_url,
                       img_url=random_cafe.img_url,
                       location=random_cafe.location,
                       seats=random_cafe.seats,
                       coffee_price=random_cafe.coffee_price,
                       has_sockets=random_cafe.has_sockets,
                       has_toilet=random_cafe.has_toilet,
                       has_wifi=random_cafe.has_wifi,
                       can_take_calls=random_cafe.can_take_calls)


# all cafes
@app.route("/all")
def all():
    # fetch all cafes
    with app.app_context():
        all_cafes = db.session.execute(db.select(Cafe)).scalars().all()
        db.session.commit()
        # return json
        list_of_all_cafes = []
        for each_cafe in all_cafes:
            each_cafe_dict = dict(name=each_cafe.name,
                                  map_url=each_cafe.map_url,
                                  img_url=each_cafe.img_url,
                                  location=each_cafe.location,
                                  seats=each_cafe.seats,
                                  coffee_price=each_cafe.coffee_price,
                                  has_sockets=each_cafe.has_sockets,
                                  has_toilet=each_cafe.has_toilet,
                                  has_wifi=each_cafe.has_wifi,
                                  can_take_calls=each_cafe.can_take_calls)
            list_of_all_cafes.append(each_cafe_dict)
        return jsonify(list_of_all_cafes)


# search for a particular cafe at some location
@app.route("/search")
def search():
    location = request.args.get("loc")
    # fetch cafe at this location
    with app.app_context():
        location_cafes = db.session.execute(db.select(Cafe).filter_by(location=location)).scalars().all()
        if location_cafes:
            list_of_location_cafes = []
            for each_cafe in location_cafes:
                each_cafe_dict = dict(name=each_cafe.name,
                                      map_url=each_cafe.map_url,
                                      img_url=each_cafe.img_url,
                                      location=each_cafe.location,
                                      seats=each_cafe.seats,
                                      coffee_price=each_cafe.coffee_price,
                                      has_sockets=each_cafe.has_sockets,
                                      has_toilet=each_cafe.has_toilet,
                                      has_wifi=each_cafe.has_wifi,
                                      can_take_calls=each_cafe.can_take_calls)
                list_of_location_cafes.append(each_cafe_dict)
            return jsonify(list_of_location_cafes)
        else:
            return jsonify({"Not Found": "Sorry, we don't have a cafe at that location."})


# HTTP POST - Create Record
# add new cafe
@app.route("/add", methods=["GET", "POST"])
def add_cafe():
    with app.app_context():
        new_cafe = Cafe(name=request.form.get("name"),
                        map_url=request.form.get("map_url"),
                        img_url=request.form.get("img_url"),
                        location=request.form.get("location"),
                        seats=request.form.get("seats"),
                        has_toilet=bool(int(request.form.get("has_toilet"))),
                        has_wifi=bool(int(request.form.get("has_wifi"))),
                        has_sockets=bool(int(request.form.get("has_sockets"))),
                        can_take_calls=bool(int(request.form.get("can_take_calls"))),
                        coffee_price=request.form.get("coffee_price"))
        db.session.add(new_cafe)
        db.session.commit()
        return jsonify({"success": "Successfully added the new cafe."})


# HTTP PUT/PATCH - Update Record
# update cafe price
@app.route("/update-price/<int:cafe_id>", methods=["PATCH"])
def update_price(cafe_id):
    new_price = request.args.get("new_price")
    with app.app_context():
        old_cafe = db.session.execute(db.select(Cafe).filter_by(id=cafe_id)).first()
        if old_cafe:
            old_cafe.coffee_price = new_price
            db.session.commit()
            return jsonify({"success": "Successfully updated the price."})
        else:
            return jsonify(error={"Not Found": "Sorry a cafe with that id was not found in the database."}),


# HTTP DELETE - Delete Record
# close cafe
@app.route("/report-closed/<int:cafe_id>", methods=["DELETE"])
def report_close(cafe_id):
    api_key = request.args.get("api_key")
    if api_key == API_KEY:
        with app.app_context():
            closed_cafe = db.session.execute(db.select(Cafe).filter_by(id=cafe_id)).first()
            print(closed_cafe)
            if closed_cafe:
                db.session.delete(closed_cafe)
                db.session.commit()
                return jsonify({"success": "Successfully deleted the cafe."})
            else:
                return jsonify({"Not Found": "Sorry a cafe with that id was not found in the database."})
    else:
        return jsonify({"error": "Sorry, the api_key is wrong."})


if __name__ == '__main__':
    app.run(debug=True)
