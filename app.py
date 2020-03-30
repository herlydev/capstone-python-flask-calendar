from flask import Flask, request, jsonify
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import os



app = Flask(__name__)
CORS(app)

basedir = os.path.abspath(os.path.dirname(__file__))
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + os.path.join(basedir, "app.sqlite")

db = SQLAlchemy(app)
ma = Marshmallow(app)

class Lead(db.Model):
    __tablename__ = "leads"
    id = db.Column(db.Integer, primary_key=True)
    fname = db.Column(db.String(25), nullable=False)
    lname = db.Column(db.String(25), nullable=False)
    phone = db.Column(db.String(10), nullable=False)
    email = db.Column(db.String(130), unique=True, nullable=False)

    def __init__(self, fname, lname, phone, email):
        self.fname = fname
        self.lname = lname
        self.phone = phone
        self.email = email

class LeadSchema(ma.Schema):
    class Meta:
        fields = ("id", "fname", "lname", "phone", "email")

lead_schema = LeadSchema()
leads_schema = LeadSchema(many=True)

@app.route("/lead", methods=["POST"])
def add_lead():
    fname = request.json["fname"]
    lname = request.json["lname"]
    phone = request.json["phone"]
    email = request.json["email"]

    new_lead = Lead(fname, lname, phone, email)

    db.session.add(new_lead)
    db.session.commit()

    lead = Lead.query.get(new_lead.id)
    return lead_schema.jsonify(lead)

@app.route("/leads", methods=["GET"])
def get_leads():
    all_leads = Lead.query.all()
    results = leads_schema.dump(all_leads)

    return jsonify(results)

@app.route("/lead/<id>", methods=["DELETE"])
def delete_lead(id):
    lead = Lead.query.get(id)
    db.session.delete(lead)
    db.session.commit()

    return jsonify("Lead Deleted")

 
# @app.route('/')
# def home():
#     return 'Home Page'

# @app.route('/contact')
# def home():
#     return 'Contact Us'

if __name__ == '__main__':
    app.debug = True
    app.run()