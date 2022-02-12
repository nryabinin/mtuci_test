import requests
from flask import Flask, render_template, request
import psycopg2

app = Flask(__name__)

conn = psycopg2.connect(database="service_db", user="postgres", password="123456", host="localhost", port="5432")

cursor = conn.cursor()


@app.route('/login/', methods=['POST'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')
    if not username or not password:
        return render_template("empty.html")

    try:
        cursor.execute(f"SELECT * FROM service.users WHERE login='{str(username)}' AND password='{str(password)}'")
        records = list(cursor.fetchall())
        return render_template('account.html', full_name=records[0][1], login=str(username), password=str(password))
    except Exception as e:
        cursor.execute(f"SELECT * FROM service.users WHERE login='{str(username)}' AND password='{str(password)}'")
        return render_template('nouser.html')





@app.route('/login/', methods=['GET'])
def index():
    return render_template('login.html')

