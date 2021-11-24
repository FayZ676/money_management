import mysql.connector
from datetime import datetime
from flask import Flask, render_template, request
from flask_mysqldb import MySQL


app = Flask(__name__, template_folder='templates')

# app.config['MYSQL_HOST'] = ''
# app.config['MYSQL_USER'] = ''
# app.config['MYSQL_PASSWORD'] = ''
# app.config['MYSQL_DB'] = ''
# app.config['MYSQL_HOST'] = ''

@app.route("/", methods = ["GET", "POST"])
def index():
    if request.method == "POST":
        expenseDetails = request.form
        item = expenseDetails['item']
        price = expenseDetails['price']
        category = expenseDetails['category']
        date = expenseDetails['date']

        insert(item, price, category, date)
        return 'success'

    return render_template("index.html")

if __name__ == '__main__':
    app.run(debug=True)

db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "root12345",
    database = "expenses",
    auth_plugin='mysql_native_password'
)

mycursor = db.cursor()

# Create the entire database
def create_database():
    sql = "CREATE DATABASE expenses"
    mycursor.execute(sql)

# Add a table to the database
def create_table():
    sql = "CREATE TABLE Exp1 (item VARCHAR(50) NOT NULL, price FLOAT(6, 2) NOT NULL, category ENUM('Groceries', 'Rent', 'Entertainment', 'Personal', 'Other') NOT NULL, date DATE NOT NULL)"
    mycursor.execute(sql)

# Delete a table from the database
def delete_table():
    sql = "DROP TABLE Exp1"
    mycursor.execute(sql)

# Display database description
def describe_database():
    sql = "DESCRIBE Exp1"
    mycursor.execute(sql)
    for x in mycursor:
        print(x)

# Insert an expense into the database
def insert(item, price, category, date):
    sql = "INSERT INTO Exp1 (item, price, category, date) VALUES (%s, %s, %s, %s)"
    val = (item, price, category, date)
    mycursor.execute(sql, val)

# Get all entries from the database
def get_all():
    sql = "SELECT * FROM Exp1 ORDER BY date DESC"
    mycursor.execute(sql)
    for x in mycursor:
        print(x)

# Get a given category from the database
def get_category(category):
    sql = "SELECT * FROM Exp1 WHERE category = %(category)s ORDER BY date DESC"
    mycursor.execute(sql, {'category' : category})
    for x in mycursor:
        print(x)

# delete_table()
# create_table()
# insert('apples', 2.50, 'Groceries')
# insert('Gym Membership', 35.25, 'Personal')
# get_all()
# get_category('Groceries')

db.commit()





