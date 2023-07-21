from datetime import datetime
from . import db 
from flask_login import UserMixin
from sqlalchemy.sql import func

class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(10000))
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))
    notes = db.relationship('Note')

class Document(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    campaign_id = db.Column(db.Integer, db.ForeignKey('campaign.id'), nullable=False)
    document_name = db.Column(db.String(100), nullable=False)
    document_type = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)
    include_agent_contact = db.Column(db.Boolean, default=False, nullable=False)
    agent_name = db.Column(db.String(100), nullable=True)
    agent_email = db.Column(db.String(120), nullable=True)
    agent_mobile = db.Column(db.String(20), nullable=True)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

class Campaign(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    #user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    property_address = db.Column(db.String(255), nullable=False)
    rental_amount = db.Column(db.Float, nullable=True)
    sales_price = db.Column(db.Float, nullable=True)
    home_size = db.Column(db.Float, nullable=True)
    type = db.Column(db.String(50), nullable=True)
    market_date = db.Column(db.Date, nullable=False)
    property_type = db.Column(db.String(50), nullable=False)
    bedrooms = db.Column(db.Integer, nullable=False)
    bathrooms = db.Column(db.Integer, nullable=False)
    car_spaces = db.Column(db.Integer, nullable=False)
    furnishing = db.Column(db.String(50), nullable=False)
    airconditioning = db.Column(db.String(50), nullable=False)
    pet_friendly = db.Column(db.String(50), nullable=False)
    amenity_pool = db.Column(db.Boolean, default=False)
    amenity_gym = db.Column(db.Boolean, default=False)
    amenity_spa = db.Column(db.Boolean, default=False)
    amenity_communal_entertaining = db.Column(db.Boolean, default=False)
    amenity_communal_cooking = db.Column(db.Boolean, default=False)
    documents = db.relationship('Document', backref='campaign', lazy=True)