from flask import Flask, render_template, redirect,url_for,request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from werkzeug.utils import secure_filename
import os
UPLOAD_FOLDER = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'static/uploads/')
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
db = SQLAlchemy(app)

# USER INTERFACE ROUTES
@app.route("/blog-list")
def blog_list():
    blogs = Blog.query.all()
    return render_template("blog-list.html",blogs=blogs)
    return render_template("blog-list.html", blogs=blogs)

@app.route("/about-us")
def about_us():
    return render_template("about-us.html")

@app.route("/blog-detail")
def blog_detail():
    return render_template("blog-detail.html")

@app.route("/checkout")
def checkout():
    return render_template("checkout.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/index")
def index():
    return render_template("index.html")

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/product-detail")
def product_detail():
    return render_template("product-detail.html")

@app.route("/product-list")
def product_list():
    return render_template("product-list.html")

@app.route("/register")
def register():
    return render_template("register.html")

@app.route("/shopping-cart")
def shopping_cart():
    return render_template("shopping-cart.html")



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

# ADMIN PANEL ROUTES

@app.route("/admin-blog-add", methods=['GET', 'POST']) 
def admin_blog_add():
    if request.method == 'POST':
        file = request.files['file']
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        blog = Blog(
            title = request.form['title'],
            short_description = request.form['short-desc'], 
            description = request.form['desc'],
            image = filename
        )
        db.session.add(blog)
        db.session.commit()
        return redirect(url_for('blog_list'))
    return render_template ("admin/blog-add.html")

if __name__ == "__main__" :
    app.run(debug=True)