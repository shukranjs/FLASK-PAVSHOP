from flask import render_template,url_for,redirect,request
from app import app
from app import db
from app.models import Blog
from werkzeug.utils import secure_filename
import os
UPLOAD_FOLDER = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'static/uploads/')


# USER INTERFACE ROUTES
@app.route("/blog-list")
def blog_list():
    blogs = Blog.query.all()
    return render_template("blog-list.html",blogs=blogs)


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
