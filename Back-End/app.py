from flask import Flask,jsonify
from flask_mysqldb import MySQL
from flask_cors import CORS

app = Flask(__name__)
CORS(app , resources={r"/*": {"origins": "*"}})

#MySQL DB connection configuration;
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '123456'
app.config['MYSQL_PORT'] = 13306
app.config['MYSQL_DB'] = 'user_info'

mysql = MySQL(app)


@app.route('/users')
def users():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM users")
    fetchdata = cur.fetchall()
    cur.close()
    return jsonify(fetchdata)

if __name__ == "__main__":
        app.run(debug=True)
