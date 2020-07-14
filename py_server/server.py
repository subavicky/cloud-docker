from flask import Flask
import psycopg2

app = Flask(__name__)

@app.route("/")
def index():
    con = psycopg2.connect(database="postgres", user="postgres", password="postgres", host="pgsql", port="5432")
    cur = con.cursor()
    # cur.execute("INSERT into test (id, name) values (0, 'suba')")
    # con.commit()
    # cur = con.cursor()
    try:
        cur.execute("SELECT * from test")
    except:
        con.close()
        con = psycopg2.connect(database="postgres", user="postgres", password="postgres", host="pgsql", port="5432")
        cur = con.cursor()
        cur.execute("CREATE table test (id int primary key, name text)")
        con.commit()
        cur = con.cursor()
        cur.execute("INSERT into test (id, name) values (0, 'suba')")
        con.commit()
        cur = con.cursor()
        cur.execute("SELECT * from test")

    rows = cur.fetchall()
    name = ""
    for row in rows:
        name = row[1]
    return "Hello {}".format(name)

if __name__ == "__main__":
    app.run("0.0.0.0", port=11000, debug=True)
