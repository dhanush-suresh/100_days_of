from flask import Flask, render_template, request
import mysql.connector
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

def get_db_connection():
    return mysql.connector.connect(
        host=app.config["DB_HOST"],
        user=app.config["DB_USER"],
        password=app.config["DB_PASSWORD"],
        database=app.config["DB_NAME"]
    )

@app.route('/')
def index():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users LIMIT 5")
    rows = cursor.fetchall()
    cursor.close()
    conn.close()
    return render_template('index.html', rows=rows)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
