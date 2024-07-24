from flask import Flask, render_template
import sqlite3
from sqlite3 import Error

app = Flask(__name__)
DATABASE = "toydatabase.db"

def create_connection(db_file):
    try:
        connection = sqlite3.connect(db_file)
        return connection
    except Error as e:
        print(e)
    return None

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=81)