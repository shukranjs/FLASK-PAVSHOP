from datetime import datetime
from app import db

class Blog(db.Model):

    __tablename__ = 'blog'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    short_description = db.Column(db.String(127), nullable=False)
    description = db.Column(db.Text, nullable=False)
    published_at = db.Column(db.DateTime, default = datetime.utcnow)
    image = db.Column(db.String(20), default='static/uploads/download.jpeg')

class Product(db.Model):

    __tablename__='product'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), nullable=False)
    price = db.Column(db.String(100),nullable = False)
    designer = db.Column(db.String(100),nullable= True)
    brand = db.Column(db.String(120),nullable= False)
    short_description = db.Column(db.String(100),nullable = False)
    description = db.Column(db.Text, nullable=False)
    image = db.Column(db.String(20), nullable = False)






    def __repr__(self):
        return self.title