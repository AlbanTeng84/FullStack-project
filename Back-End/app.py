from flask import Flask,jsonify
from flask_mysqldb import MySQL
from flask_cors import CORS

app = Flask(__name__)
CORS(app , resources={r"/*": {"origins": "*"}})

#MySQL DB connection configuration;
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'root'
app.config['MYSQL_DB'] = 'db'
mysql = MySQL(app)

@app.route('/jobs')
def jobs():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM jobs")
    fetchdata = cur.fetchall()
    cur.close()
    return jsonify(fetchdata)
    
 

if __name__ == "__main__":
    app.run(debug=True)
