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

# HOME WEBPAGE
@app.route('/')
def render_home():
    return render_template("index.html")

# ALL DATA WEBPAGE
@app.route('/alldata')
def render_alldata():
    query = "SELECT Description, Location, Universe, Condition, DecadeMade, Size, PricePaid FROM toytable"
    con = create_connection(DATABASE)
    cur = con.cursor()

    # Query the DATABASE
    cur.execute(query)
    toy_list = cur.fetchall()
    con.close()
    print(toy_list)
    return render_template('alldata.html', toys=toy_list)

# DECADE MADE WEBPAGE
@app.route('/decademade')
def render_decademade():
    query = "SELECT DISTINCT DecadeMade, Description FROM toytable ORDER BY DecadeMade ASC"
    con = create_connection(DATABASE)
    cur = con.cursor()

    # Query the DATABASE
    cur.execute(query)
    toy_list = cur.fetchall()
    con.close()
    print(toy_list)
    return render_template('decademade.html', toys=toy_list)

# LOCATION WEBPAPGE
@app.route('/location')
def render_location():
    query = "SELECT Description, Location FROM toytable"
    con = create_connection(DATABASE)
    cur = con.cursor()

    # Query the DATABASE
    cur.execute(query)
    toy_list = cur.fetchall()
    con.close()
    print(toy_list)
    return render_template('location.html', toys=toy_list)

# UNIVERSE WEBPAGE
@app.route('/universe')
def render_universe():
    query = "SELECT Description, Universe FROM toytable"
    con = create_connection(DATABASE)
    cur = con.cursor()

    # Query the DATABASE
    cur.execute(query)
    toy_list = cur.fetchall()
    con.close()
    print(toy_list)
    return render_template('universe.html', toys=toy_list)

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=81)