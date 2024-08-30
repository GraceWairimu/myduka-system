from flask import Flask, render_template, request, redirect, url_for, flash,session
from dbservice import get_data, insert_products, insert_sales, sales_per_product, profit_per_product, sales_per_day, profits_per_day, register_users, check_email
from flask_bcrypt import Bcrypt  # for hashing the password


# Create Flask instance
# Configure your application
# Define routes
app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
bcrypt = Bcrypt(app)  # creating a bcrypt object

# URL-uniform resource locator
# https://techcamp.co.ke

# Route-used to connect url with a function
# https://techcamp.co.ke/
# https://techcamp.co.ke/about-us
# You must have a function below.

# ALL HTML files are placed inside the Templates folder.
# ALL CSS and JavaScript files are placed inside the Static Folder
# JINJA2-
# used to pass pyton variables and operations to front end.
# When passing variables we use {{}} inside an element.
# When passing operations we use {% %} e.g {%if 2>1 %} {% endif %}:if statement end {%endfor %}:for loop ending

# creating a route


@app.route("/")
def index():
    # return "Hello,World!"
    return render_template("index.html")

# Home route


@app.route("/home")
def home():
    return render_template("home.html")

# Products route


@app.route("/products")
def products():
    prods = get_data("products")
    # print(prods)
    return render_template("products.html", product=prods)

# Adding products


@app.route("/add_products", methods=["POST", "GET"])
def add_products():
    # Check method(checks if there's any data entered into the form)
    if request.method == "POST":
        # request data from the form
        pname = request.form['productname']
        bprice = request.form["buyingprice"]
        sprice = request.form["sellingprice"]
        squantity = request.form["stockquantity"]

    # insert products
    new_prod = (pname, bprice, sprice, squantity)
    insert_products(new_prod)
    # url_for takes in the function name of the route you want to be redirected to
    return redirect(url_for("products"))


# http methods-techniques used to send(post method),fetch(get method),update(put method),delete(delete method) data from the browser

# Sales route
@app.route("/sales")
def sales():
    sale = get_data("sales")
    products = get_data("products")
    # print(sale)
    return render_template("sales.html", sale=sale, prods=products)

# Adding Sales


@app.route("/add_sales", methods=["POST", "GET"])
def add_sales():
    # Check method(checks if there's any data entered into the form)
    if request.method == "POST":
        # request data from the form
        pid = request.form["productid"]
        quantity = request.form["quantity"]
        # created_at = request.form["created_at"]
    # insert sales
    new_sale = (pid, quantity)
    insert_sales(new_sale)
    return redirect(url_for("sales"))

# Dashboard route


@app.route("/dashboard")
def dashboard():
    if "email" not in session:
        return redirect(url_for("login"))
    else:
        # Sales per product
        s_prods = sales_per_product()
        # print(s_prods)
        names = []
        sales = []

        for i in s_prods:
            names.append(i[1])
            sales.append(i[2])

        # Profit per product
        p_prods = profit_per_product()
        # print(p_prods)
        prnames = []
        profit = []

        for x in p_prods:
            prnames.append(x[1])
            profit.append(x[2])

        # Sales per Day
        s_days = sales_per_day()
        sdate = []
        sales = []

        for m in s_days:
            sdate.append(str(m[0]))
            sales.append(m[1])

        # Profit per Day
        p_days = profits_per_day()
        pdate = []
        profit = []

        for p in p_days:
            pdate.append(str(p[0]))
            profit.append(p[1])

    return render_template("dashboard.html", names=names, sales=sales, profit=profit, prnames=prnames, sdate=sdate, pdate=pdate)


# Registering User Route
@app.route("/register", methods=["POST", "GET"])
def register():
    if request.method == "POST":
        # get form data
        fname = request.form['full_name']
        email = request.form["email"]
        password = request.form["password"]

        # Hashing the password
        hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')

        x = check_email(email)
        if x==None:
            # insert user
            new_user = (fname, email, hashed_password)
            register_users(new_user)
            return redirect(url_for("login"))
        else:
            # return "Email already exists"
            flash("Email already exists,login")
            return redirect(url_for("login"))
    return render_template("register.html")

# Login page route


@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        # get data from the form
        email = request.form["email"]
        password = request.form["password"]

        # check email(user) alone first
        user = check_email(email)
        if user == None:
            flash("Email does not exist")
            return redirect(url_for("register"))
        else:
            # check password
            if bcrypt.check_password_hash(user[-1],password):
                flash("Login successful")
                session["email"]=email
                return redirect(url_for("dashboard"))
            else:
                flash("Password is incorrect")
    
    return render_template("login.html")

@app.route("/logout")
def logout():
    session.pop("email",None)
    return redirect(url_for("login"))

# we are using the variable app to run #Should always be the last thing
app.run(debug=True)

# Create HTML files for each route=home.html,products.html,sales.html,dashboard.html
# Create relevant content for each file
# https://youtu.be/mqhxxeeTbu0?si=cJhiVcGFT1pXAkAM===use this to learn more about flask


# flash messages
# login.html
# route to login user
