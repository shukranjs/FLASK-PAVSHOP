from flask import Flask, render_template, redirect,url_for
app = Flask(__name__)

@app.route("/")
@app.route("/blog-list")
def blog_list():
    return render_template("blog-list.html")

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
    
if __name__ == "__main__" :
    app.run(debug=True)