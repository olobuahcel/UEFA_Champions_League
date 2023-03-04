

import sqlite3
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/league')
def league():
    # open the connection to the database
    conn = sqlite3.connect('UCLQuarterFinals.db')
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    cur.execute("select * from league")
    rows = cur.fetchall()
    conn.close()
    return render_template('league.html', rows=rows)

@app.route('/leagueID/<ID>')
def leagueID(ID):
    # open the connection to the database
    conn = sqlite3.connect('UCLQuarterFinals.db')
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    cur.execute("select * from league where ID=?",([ID]))
    rows = cur.fetchall()
    conn.close()
    return render_template('league.html', rows=rows)

@app.route('/locations')
def locations():
    # open the connection to the database
    conn = sqlite3.connect('UCLQuarterFinals.db')
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    cur.execute("select * from locations")
    rows = cur.fetchall()
    conn.close()
    return render_template('locations.html', rows=rows)
