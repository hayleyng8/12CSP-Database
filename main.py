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
    query = "SELECT Description, Location, ToyLine, Condition, DecadeMade, Size, PricePaid, image FROM toytable"
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


# Toy Line WEBPAGE
@app.route('/toyline')
def render_toyline():
    return render_template('toyline.html')


# d.c webpage
@app.route('/dc')
def render_dc():
    query = "SELECT ToyLine, Description, image FROM toytable WHERE ToyLine = 'D.C';"
    con = create_connection(DATABASE)
    cur = con.cursor()

    # Query the DATABASE
    cur.execute(query)
    dc_list = cur.fetchall()
    con.close()
    print(dc_list)
    return render_template("/toyline/dc.html", dc_toys=dc_list)

# fast & furious webpage
@app.route('/fandf')
def render_fandf():
    query = "SELECT ToyLine, Description, image FROM toytable WHERE ToyLine = 'Fast & Furious';"
    con = create_connection(DATABASE)
    cur = con.cursor()

    # Query the DATABASE
    cur.execute(query)
    fandf_list = cur.fetchall()
    con.close()
    print(fandf_list)
    return render_template("/toyline/fandf.html", fandf_toys=fandf_list)


# marvel webpage
@app.route('/marvel')
def render_marvel():
    query = "SELECT ToyLine, Description, image FROM toytable WHERE ToyLine = 'Marvel';"
    con = create_connection(DATABASE)
    cur = con.cursor()

    # Query the DATABASE
    cur.execute(query)
    marvel_list = cur.fetchall()
    con.close()
    print(marvel_list)
    return render_template("/toyline/marvel.html", marvel_toys=marvel_list)


# starwars webpage
@app.route('/starwars')
def render_starwars():
    query = "SELECT ToyLine, Description, image FROM toytable WHERE ToyLine = 'Star Wars';"
    con = create_connection(DATABASE)
    cur = con.cursor()

    # Query the DATABASE
    cur.execute(query)
    starwars_list = cur.fetchall()
    con.close()
    print(starwars_list)
    return render_template("/toyline/starwars.html", starwars_toys=starwars_list)


# terminator webpage
@app.route('/terminator')
def render_terminator():
    query = "SELECT ToyLine, Description, image FROM toytable WHERE ToyLine = 'Terminator';"
    con = create_connection(DATABASE)
    cur = con.cursor()

    # Query the DATABASE
    cur.execute(query)
    terminator_list = cur.fetchall()
    con.close()
    print(terminator_list)
    return render_template("/toyline/terminator.html", terminator_toys=terminator_list)


# top gun maverick webpage
@app.route('/topgun')
def render_topgun():
    query = "SELECT ToyLine, Description, image FROM toytable WHERE ToyLine = 'Top Gun';"
    con = create_connection(DATABASE)
    cur = con.cursor()

    # Query the DATABASE
    cur.execute(query)
    topgun_list = cur.fetchall()
    con.close()
    print(topgun_list)
    return render_template("/toyline/topgun.html", topgun_toys=topgun_list)


# transformers webpage
@app.route('/transformers')
def render_transformers():
    query = "SELECT ToyLine, Description, image FROM toytable WHERE ToyLine = 'Transformers';"
    con = create_connection(DATABASE)
    cur = con.cursor()

    # Query the DATABASE
    cur.execute(query)
    transformers_list = cur.fetchall()
    con.close()
    print(transformers_list)
    return render_template("/toyline/transformers.html", transformers_toys=transformers_list)


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

    query = "SELECT Description, Location, ToyLine, Condition, DecadeMade, Size, PricePaid, image FROM toytable ORDER BY " + sort + " " + order
    con = create_connection(DATABASE)
    cur = con.cursor()

    cur.execute(query)
    toy_list = cur.fetchall()
    con.close()

    return render_template('alldata.html', toys=toy_list, order=new_order)


# Sorting the Toyline in the Toy line webpage
@app.route('/sort/toyline')
def render_sorttoyline():
    sort = request.args.get('sort')
    order = request.args.get('order', 'asc')

    if order == 'asc':
        new_order = 'desc'
    else:
        new_order = 'asc'

    query = "SELECT ToyLine, Description, image FROM toytable ORDER BY " + sort + " " + order

    con = create_connection(DATABASE)
    cur = con.cursor()

    cur.execute(query)
    toy_list = cur.fetchall()
    con.close()

    return render_template('toyline.html', toys=toy_list, order=new_order)


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
    query = "SELECT Description, Location, ToyLine, Condition, DecadeMade, Size, PricePaid FROM toytable WHERE Description LIKE ? OR Location LIKE ? OR ToyLine LIKE ? OR Condition LIKE ? OR DecadeMade LIKE ? or Size LIKE ? or PricePaid LIKE ?"
    search = "%" + search + "%"
    con = create_connection(DATABASE)
    cur = con.cursor()
    cur.execute(query,(search, search, search, search, search, search, search))
    toy_list = cur.fetchall()
    con.close()

    return render_template("search.html", searches=toy_list, title=title)


if __name__ == '__main__':
  app.run(host='0.0.0.0', port=81)