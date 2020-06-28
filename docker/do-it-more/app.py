import os
from flask import Flask
import json
import pymysql

app = Flask(__name__)


def connection():
    host = os.environ['MYSQL_HOST']
    user = os.environ['MYSQL_USER']
    password = os.environ['MYSQL_PASSWORD']
    db = 'information_schema'
    conn = pymysql.connect(host=host, user=user, \
            password=password, db=db, \
            cursorclass=pymysql.cursors.DictCursor)

    return conn


@app.route('/api')
def hello():
    conn = connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM TABLES")
    result = cur.fetchall()
    return str(result)


if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)

