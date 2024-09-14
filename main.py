from flask import Flask, render_template, request
#from flask import Flask, render_template, request, session
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

# attic webpage
@app.route('/attic')
def render_attic():
    query = "SELECT Location, Description, image FROM toytable WHERE Location = 'Attic';"
    con = create_connection(DATABASE)
    cur = con.cursor()

    # Query the DATABASE
    cur.execute(query)
    attic_list = cur.fetchall()
    con.close()
    print(attic_list)
    return render_template("/location/attic.html", attic_toys=attic_list)

# garage webpage
@app.route('/garage')
def render_garage():
    query = "SELECT Location, Description, image FROM toytable WHERE Location = 'Garage';"
    con = create_connection(DATABASE)
    cur = con.cursor()

    # Query the DATABASE
    cur.execute(query)
    garage_list = cur.fetchall()
    con.close()
    print(garage_list)
    return render_template("/location/garage.html", garage_toys=garage_list)

# toy room webpage
@app.route('/toyroom')
def render_toyroom():
    query = "SELECT Location, Description, image FROM toytable WHERE Location = 'Toy Room';"
    con = create_connection(DATABASE)
    cur = con.cursor()

    # Query the DATABASE
    cur.execute(query)
    toyroom_list = cur.fetchall()
    con.close()
    print(toyroom_list)
    return render_template("/location/toyroom.html", toyroom_toys=toyroom_list)


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


# Sorting the location on the all data webpage
@app.route('/sort/location')
def render_sortlocation():
    sort = request.args.get('sort')
    order = request.args.get('order', 'asc')

    if order == 'asc':
        new_order = 'desc'
    else:
        new_order = 'asc'

    query = "SELECT Description, Location, Universe, Condition, DecadeMade, Size, PricePaid, image FROM toytable ORDER BY " + sort + " " + order
    con = create_connection(DATABASE)
    cur = con.cursor()

    cur.execute(query)
    toy_list = cur.fetchall()
    con.close()

    return render_template('alldata.html', toys=toy_list, order=new_order)


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


# LOCATION TRIAL
"""
@app.route('/location', methods=['GET', 'POST'])
def render_location():
    if request.method == 'POST':
        #content = request.form['content']
        content = "This is the updated content from the server."
    else:
        content = "This is the original content."
        #content = None
    return render_template('location.html', content=content)
"""
#LOCATION TRIAL SWAPPING BUTTON
"""
app.secret_key = 'your_secret_key'

@app.route('/location', methods=['GET', 'POST'])
def render_location():
    if 'content' not in session:
        session['content'] = "This is the original content."

    if request.method == 'POST':
        if session['content'] == "This is the original content.":
            session['content'] = "This is the updated content from the server."
        else:
            session['content'] = "This is the original content."
    return render_template('location.html', content=session['content'])
"""

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=81)