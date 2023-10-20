##
from flask import Flask
from db.db_connection import DB_connection

app = Flask(__name__)
db = DB_connection()

@app.route("/")
def home():
	return "<h4>This is simple service</h4>" 

@app.route("/task/")
def task():
	res = db.select_all_tasks()
	return f"{res}"


if __name__ == "__main__":
	app.run(debug=True)