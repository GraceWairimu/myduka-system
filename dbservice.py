import psycopg2

# Connecting to the database

connect = psycopg2.connect(
    dbname="my_duka",
    password="1234",
    user="postgres",
    host="localhost",
    port=5432
)

# Define the cursor-perform database operations

curr = connect.cursor()

# Function to fetch products
# def get_products():
#     query="select * from products where productid=1"
#     curr.execute(query)
#     prods=curr.fetchall()
#     return prods

# products=get_products()
# print(products)

# Function to fetch sales
# def get_sales():
#     query="select datetime from sales"
#     curr.execute()
#     sale=curr.fetchall()
#     return sale

# sales=get_sales()
# print(sales)

# Create one function that will fetch data from the database
# -first identify the differences between the products function and sales function


def get_data(table_name):

    query = f"Select * from {table_name}"
    curr.execute(query)
    tb = curr.fetchall()
    return tb

# prods=get_data("products")
# print(prods)
# sales=get_data("sales")
# print(sales)


# Insert data
# psql=> dbservice

# Write a query to insert products first to know whether it is running
def insert_products():
    query = "insert into products(name,buying_price,selling_price,stock_quantity)values('Chumvi',30,80,70)"
    curr.execute(query)
    connect.commit()


# prods=get_data("products")
# print(prods)
# Write a query to make sales

def insert_products(values):
    query = "insert into products(name,buying_price,selling_price,stock_quantity)values(%s,%s,%s,%s)"
    curr.execute(query, values)
    connect.commit()


value = ('Kamande', 220, 350, 18)
# insert_products(value)
# prods=get_data("products")
# print(prods)


def insert_sales(values):
    query = "insert into sales(productid,quantity,created_at) values(%s,%s,now())"
    curr.execute(query, values)
    connect.commit()

# val=((21,66))
# x=get_data(val)
# print(x)
# print(sales)

# Write a query and a function to get profit per product
# psql=>dbservice


def profit_per_product():
    query = "SELECT products.productid, name, sum((selling_price - buying_price)* quantity) AS profit_per_product FROM  products inner join sales on sales.productid=products.productid group by  products.productid,name;"
    curr.execute(query)
    data = curr.fetchall()
    return data

profitper_product=profit_per_product()
# print(profitper_product)

# Write a query and a function to get sales per product
# psql=>dbservice


def sales_per_product():
    query = "SELECT sales.productid, products.name, SUM((sales.quantity)* products.selling_price) AS total_sales FROM sales INNER JOIN products ON products.productid = sales.productid GROUP BY sales.productid, products.name ORDER BY total_sales DESC;"
    curr.execute(query)
    data = curr.fetchall()
    return data

salesper_product=sales_per_product()
# print(salesper_product)

# Write a query and a function to get sales per day


def sales_per_day():
    query = "SELECT date(sales.created_at) as Day, sum((selling_price - buying_price)* quantity) AS profit_per_day FROM  products inner join sales on sales.productid=products.productid group by  Day order by Day;"
    curr.execute(query)
    data = curr.fetchall()
    return data

salesper_day=sales_per_day()
# print(salesper_day)


# Write a query and a function to get profit per day
def profits_per_day():
    query = "SELECT Date(sales.created_at) as Day, sum((selling_price - buying_price)* quantity) AS profit_per_day FROM  products inner join sales on sales.productid=products.productid group by  Day order by Day;"
    curr.execute(query)
    data = curr.fetchall()
    return data

profitper_day=profits_per_day()
# print(profitper_day)

# function to insert users
def register_users(values):
    query = "insert into users(full_name,email,password)values(%s,%s,%s)"
    curr.execute(query, values)
    connect.commit()


# Query to check email existence on the database using exist
# "select 'The email exists'  where exists(select 1 from users where email='matt@gmail.com');"
# # OR
# "select exists(select 1 from users where email='matt@gmail.com');"
# # OR
# "select * from users where email='matt@gmail.com';"  #when using this,ensure you pass the email as a string i.e curr.execute(querry,(email,))

# Function to check email
def check_email(email):
    # query="select 'The email exists'  where exists(select 1 from users where email= %s);"
    query="select * from users where email= %s;"
    curr.execute(query,(email,))
    data = curr.fetchone()
    if data:
        return data
    
# check_email("kim@gmail.com")

# email=check_email()
# print(email)
# login.html create a form to login user



# write a query to fetch the user with an email and password provided
# "select * from users where email='grace@gmail.com' and password='0987';"
# # Function to fetch user's email and password
# def check_email_password(email,password):
#     query="select * from users where email=%s and password=%s;"
#     curr.execute(query,(email,password))
#     data=curr.fetchall()
#     return data

# fetch_data=fetch()
# print(fetch_data)

