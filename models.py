from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Disaster(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False, unique=True)
    disaster_type = db.Column(db.String(50), nullable=False)
    date = db.Column(db.String(20), nullable=False)
    location = db.Column(db.String(100), nullable=False)

    victims = db.relationship('Victim', backref='disaster', cascade="all, delete", lazy=True)
    food_items = db.relationship('FoodItem', backref='disaster', cascade="all, delete", lazy=True)
    health_items = db.relationship('HealthItem', backref='disaster', cascade="all, delete", lazy=True)


class Victim(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    disaster_id = db.Column(db.Integer, db.ForeignKey('disaster.id'), nullable=False)


class FoodItem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    quantity = db.Column(db.Integer, nullable=False, default=0)
    disaster_id = db.Column(db.Integer, db.ForeignKey('disaster.id'), nullable=False)


class HealthItem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    quantity = db.Column(db.Integer, nullable=False, default=0)
    disaster_id = db.Column(db.Integer, db.ForeignKey('disaster.id'), nullable=False)
