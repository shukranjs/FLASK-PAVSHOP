from flask import render_template,url_for,redirect,request
from app import app
from app import db
from app.models import Blog,Product
import os
UPLOAD_FOLDER = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'static/uploads/')


# USER INTERFACE ROUTES

@app.route("/blog-list")
def blog_list():
    blogs = Blog.query.all()
    return render_template("blog-list.html",blogs=blogs)

@app.route("/product-list")
def productlist():
    products = Product.query.all()
    return render_template("product-list.html",products=products)


@app.route("/about-us")
def about_us():
    return render_template("about-us.html")

@app.route("/blog-detail/<int:id>",methods =['GET','POST'])
def blog_detail(id):
    blog = Blog.query.get_or_404(id)
    return render_template("blog-detail.html",blog = blog)

@app.route("/checkout")
def checkout():
    return render_template("checkout.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/login")
def login():
    return render_template("login.html")


@app.route("/product-detail/<int:id>")
def product_detail(id):
    product = Product.query.get_or_404(id)
    return render_template("product-detail.html",product = product)

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

@app.route("/admin-blog-list",methods=['GET','POST'])
def admin_blog_list():
    blogs = Blog.query.all()
    return render_template("admin/blog-list.html",blogs = blogs)

@app.route("/admin-blog-edit/<int:id>",methods =['GET','POST'])
def admin_blog_edit(id):
    blog = Blog.query.get(id)
    if request.method == ['POST']:
        file = request.files['file']
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        blog.title = request.form['title']
        blog.short_description = request.form['short-desc']
        blog.description = request.form['desc']
        blog.image = filename
        db.session.commit()
        return redirect(url_for('admin_blog_list'))
    return render_template('admin/blog-edit.html',blog=blog)

@app.route("/admin-blog-delete/<int:id>",methods =['GET','POST'])
def admin_blog_delete(id):
    blog = Blog.query.get(id)
    db.session.delete(blog)
    db.session.commit()
    return redirect(url_for('admin_blog_list'))

 
@app.route("/admin-add-product", methods=['GET', 'POST']) 
def admin_add_product():
    if request.method == 'POST':
        file = request.files['file']
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        product = Product(
            title = request.form['title'],
            price = request.form['price'],
            designer = request.form['designer'],
            brand = request.form['brand'],
            short_description = request.form['short-desc'], 
            description = request.form['desc'],
            image = filename
        )
        db.session.add(product)
        db.session.commit()
        return redirect(url_for('productlist'))
    return render_template ("admin/add_product.html")


@app.route("/admin-product-list",methods=['GET','POST'])
def admin_product_list():
    products = Product.query.all()
    return render_template("admin/product-list.html",products = products)



@app.route("/admin-product-edit/<int:id>",methods =['GET','POST'])
def admin_product_edit(id):
    product = Product.query.get(id)
    if request.method == ['POST']:
        file = request.files['file']
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        product.title = ['title']
        product.price = ['price']
        product.designer = ['designer']
        product.brand = ['brand']
        product.short_description = ['short-desc']
        product.description = ['desc']
        product.image = filename
        db.session.commit()
        return redirect(url_for('admin_product_list'))
    return render_template('admin/product-edit.html',product=product)

@app.route("/admin-product-delete/<int:id>",methods =['GET','POST'])
def admin_product_delete(id):
    product = Product.query.get(id)
    db.session.delete(product)
    db.session.commit()
    return redirect(url_for('admin_product_list'))
