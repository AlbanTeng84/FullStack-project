from flask import Flask,jsonify
from flask_mysqldb import MySQL
from flask_cors import CORS

app = Flask(__name__)
CORS(app , resources={r"/*": {"origins": "*"}})

#MySQL DB connection configuration - for Mac;
# app.config['MYSQL_HOST'] = 'localhost'
# app.config['MYSQL_USER'] = 'root'
# app.config['MYSQL_PASSWORD'] = '123456'
# app.config['MYSQL_PORT'] = 13306
# app.config['MYSQL_DB'] = 'user_info'

#MySQL DB connection configuration - for Win;
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'root'
app.config['MYSQL_DB'] = 'db'

mysql = MySQL(app)


@app.route('/jobs')
#@app.route('/users')
def users():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM jobs")
    #cur.execute("SELECT * FROM users")
    fetchdata = cur.fetchall()
    cur.close()
    return jsonify(fetchdata)

@app.route('/postuser')
def postuser():
    cur = mysql.connection.cursor()
    cur.execute("""INSERT INTO users VALUES(%s,%s,%s),(id,name,postion)""")
    #cur.execute("SELECT * FROM users")
    cur.close()
    return "OK"

if __name__ == "__main__":
        app.run(debug=True)
