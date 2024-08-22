from flask import Flask, render_template, request
import sqlite3
from sqlite3 import Error

#from jinja2.environment import create_cache

app = Flask(__name__)
DATABASE = "toydatabase.db"

# Creating a connection to the database
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
    query = "SELECT Description, Location, Universe, Condition, DecadeMade, Size, PricePaid, image FROM toytable"
    con = create_connection(DATABASE)
    cur = con.cursor()

    # Query the DATABASE
    cur.execute(query)
    toy_list = cur.fetchall()
    con.close()
    print(toy_list)
    return render_template('alldata.html', toys=toy_list)


# LOCATION WEBPAGE
@app.route('/location')
def render_location():
    query = "SELECT Location, Description, image FROM toytable"
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
    query = "SELECT Universe, Description, image FROM toytable"
    con = create_connection(DATABASE)
    cur = con.cursor()

    # Query the DATABASE
    cur.execute(query)
    toy_list = cur.fetchall()
    con.close()
    print(toy_list)
    return render_template('universe.html', toys=toy_list)


# VALUATION WEBPAGE
@app.route('/valuation')
def render_valuation():
    query = "SELECT Description, Condition, DecadeMade, PricePaid, image FROM toytable"
    con = create_connection(DATABASE)
    cur = con.cursor()

    cur.execute(query)
    toy_list = cur.fetchall()
    con.close()
    print(toy_list)
    return render_template('valuation.html', toys=toy_list)


# Sorting the Decade Made on the valuation webpage
@app.route('/sort/decademade')
def render_sortdecademade():
    sort = request.args.get('sort')
    order = request.args.get('order', 'asc')

    if order == "asc":
        new_order = "desc"
    else:
        new_order = "asc"

    query = "SELECT Description, Condition, DecadeMade, PricePaid, image FROM toytable ORDER BY " + sort + " " + order
    con = create_connection(DATABASE)
    cur = con.cursor()

    cur.execute(query)
    toy_list = cur.fetchall()
    con.close()

    return render_template("valuation.html", toys=toy_list, order=new_order)


# Sorting the location on the location webpage
@app.route('/sort/location')
def render_sortlocation():
    sort = request.args.get('sort')
    order = request.args.get('order', 'asc')

    if order == 'asc':
        new_order = 'desc'
    else:
        new_order = 'asc'

    query = "SELECT Location, Description, image FROM toytable ORDER BY " + sort + " " + order
    con = create_connection(DATABASE)
    cur = con.cursor()

    cur.execute(query)
    toy_list = cur.fetchall()
    con.close()

    return render_template('location.html', toys=toy_list, order=new_order)


# Sorting the Universe in the universe webpage
@app.route('/sort/universe')
def render_sortuniverse():
    sort = request.args.get('sort')
    order = request.args.get('order', 'asc')

    if order == 'asc':
        new_order = 'desc'
    else:
        new_order = 'asc'

    query = "SELECT Universe, Description, image FROM toytable ORDER BY " + sort + " " + order
    con = create_connection(DATABASE)
    cur = con.cursor()

    cur.execute(query)
    toy_list = cur.fetchall()
    con.close()

    return render_template('universe.html', toys=toy_list, order=new_order)
    

# Sorting the Condition in the valuation webpage
@app.route('/sort/condition')
def render_sortcondition():
    sort = request.args.get('sort')
    order = request.args.get('order', 'asc')

    if order == 'asc':
        new_order = 'desc'
    else:
        new_order = 'asc'

    query = "SELECT Description, Condition, DecadeMade, PricePaid, image FROM toytable ORDER BY " + sort + " " + order
    con = create_connection(DATABASE)
    cur = con.cursor()

    cur.execute(query)
    toy_list = cur.fetchall()
    con.close()

    return render_template('valuation.html', toys=toy_list, order=new_order)


# Sorting the price paid in the valuation page
@app.route('/sort/pricepaid')
def render_sortpricepaid():
    sort = request.args.get('sort')
    order = request.args.get('order', 'asc')

    if order == 'asc':
        new_order = 'desc'
    else:
        new_order = 'asc'

    query = "SELECT Description, Condition, DecadeMade, PricePaid, image FROM toytable ORDER BY " + sort + " " + order
    con = create_connection(DATABASE)
    cur = con.cursor()

    cur.execute(query)
    toy_list = cur.fetchall()
    con.close()

    return render_template('valuation.html', toys=toy_list, order=new_order)


# Search function
@app.route("/search", methods=['GET', 'POST'])
def render_search():
    search = request.form["search"]
    title = "Search for " + search
    query = "SELECT Description, Location, Universe, Condition, DecadeMade, Size, PricePaid FROM toytable WHERE Description LIKE ? OR Location LIKE ? OR Universe LIKE ? OR Condition LIKE ? OR DecadeMade LIKE ? or Size LIKE ? or PricePaid LIKE ?"
    search = "%" + search + "%"
    con = create_connection(DATABASE)
    cur = con.cursor()
    cur.execute(query,(search, search, search, search, search, search, search))
    toy_list = cur.fetchall()
    con.close()

    return render_template("search.html", searches=toy_list, title=title)

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=81)