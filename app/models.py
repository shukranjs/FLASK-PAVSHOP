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


    def __repr__(self):
        return self.title