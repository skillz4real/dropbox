import sqlite3
from datetime import datetime

from flask import Flask, render_template, request

import rpg

app = Flask(__name__)


def tuple_to_dict(t):
    d = {}
    paste_id, title, data = t
    if title:
        d.setdefault("title", title)
    else:
        d.setdefault("title", paste_id)
    d.setdefault("data", data)
    d.setdefault("id", paste_id)
    return d


@app.route("/")
def index():
    return render_template("index.html")

"""
flask routing takes the following format
/route/<var_type:var_name>
var types can be:
    - string
    - int
    - float
    - path
    - uuid
"""

@app.route('/dropbox', methods=["GET","POST"])
def dropbox():
    if request.method == 'POST':
        id = rpg.Gen((False, False, 6)) #find a way to make sure that there is no collision 
        con = sqlite3.connect('files.db')
        cursor = con.cursor()
        #value = request.form['filename']
        #title = request.form["paste-title"]
        date = str(datetime.now()).split(".")[0]
        res = cursor.execute(f"SELECT id FROM paste;")
        cursor.execute(f"INSERT INTO paste VALUES (?, ?, ?,?);",(id, title, date, value))
        #SELECT col1,col2... FROM db ORDER BY col1
        #SELECT col1 FROM db WHERE id='id_2'
        con.commit()
        con.close()

    
    con = sqlite3.connect('files.db')
    cursor = con.cursor()
    res = cursor.execute("SELECT id, title, data FROM paste")
    values = res.fetchall()
    l = []
    for value in values:
        l.append(tuple_to_dict(value))
    con.close()
    return render_template("dropbox.html", files=f)
    


if __name__=="__main__":
    
    con = sqlite3.connect("files.db")
    cursor = con.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS files(id TEXT PRIMARY KEY, title TEXT, date DATE, hash TEXT, path TEXT);")
    con.commit()
    con.close()

    app.run(debug=True, host="0.0.0.0", port=9991)

