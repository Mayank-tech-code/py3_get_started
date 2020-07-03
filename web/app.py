import psycopg2
from flask import Flask, render_template
app = Flask(__name__)

connection = psycopg2.connect(user = "postgres",
                              password = "root",
                              host = "127.0.0.1",
                              port = "5432",
                              database = "College")

def add(num1, num2):
    return num1 + num2


@app.route("/")
def home():
    contacts = []
    
    cursor = connection.cursor()
    cursor.execute('select * from student')
    rows = cursor.fetchall()
    for row in rows:
        contacts.append(row[1])

    return render_template('index.html',message="Web application tutorial!", contacts = contacts, result=add(3,4))
