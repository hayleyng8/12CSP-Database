from flask import Flask, render_template, request
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

def get_toys(toy_type):
    title = toy_type.upper()
    query = "SELECT Description, Location, Universe, Condition, DecadeMade, Size, PricePaid FROM toytable WHERE type=?"
    con = create_connection(DATABASE)
    cur = con.cursor()

    cur.execute(query,(title,))
    toy_list = cur.fetchall()
    con.close()
    print(toy_list)
    return toy_list

def get_types():
    con = create_connection(DATABASE)
    query = "SELECT DISTINCT Description, Location, Universe, Condition, DecadeMade, Size, PricePaid FROM toytable ORDER BY Description, Location, Universe, Condition, DecadeMade, Size, PricePaid ASC"
    cur = con.cursor()
    cur.execute(query)
    records = cur.fetchall()
    print(records)
    for i in range(len(records)):
        records[i] = records[i][0]
    print(records)
    return records

@app.route("/search", methods=['GET', 'POST'])
def render_search():
    search = request.form["search"]
    title = "Search for " + search
    query = "SELECT ID, Description, Location, Universe, Condition, DecadeMade, Size, PricePaid FROM toytable WHERE Description LIKE ? OR Location LIKE ? OR Universe LIKE ? OR Condition LIKE ? OR DecadeMade LIKE ? or Size LIKE ? or PricePaid LIKE ?"
    search = "%" + search + "%"
    con = create_connection(DATABASE)
    cur = con.cursor()
    cur.execute(query,(search, search, search, search, search, search, search))
    toy_list = cur.fetchall()
    con.close()

    return render_template("alldata.html", toys=toy_list, types=get_types())

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=81)