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
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'),nullable=False)

    def __repr__(self):
        return self.title



class User(db.Model):

    __tablename__='user'
    id = db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.String(120), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    address = db.Column(db.String(120), nullable=False)
    image = db.Column(db.String(20))
    password = db.Column(db.String(120))
    age = db.Column(db.Integer)
    blogs = db.relationship(Blog, backref='author', lazy=True)


    def __repr__(self):
        return self.full_name


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