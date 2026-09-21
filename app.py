from flask import Flask, render_template
import sqlite3 # For the database stuff

app = Flask(__name__)

# The path and filename for the database
DATABASE = "sc.db"

# Routes go here
@app.route('/')
def index():
    # Connect to the database file
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor() # Create the cursor
    sql = "SELECT * FROM Units" # Store a query as a string variable
    cursor.execute(sql) # Execute the query
    results = cursor.fetchall() # Fetch all the results of the query (can use fetchone too)
    db.close() # Close the database now we are done- no need to commit this time with db.commit
    return render_template('index.html',results=results) # Send the data to the template


# Routes go here
@app.route('/Search.html')
def search():
    # Connect to the database file
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor() # Create the cursor
    sql = "SELECT * FROM Units" # Store a query as a string variable
    cursor.execute(sql) # Execute the query
    results = cursor.fetchall() # Fetch all the results of the query (can use fetchone too)
    db.close() # Close the database now we are done- no need to commit this time with db.commit
    return render_template('Search.html',results=results) # Send the data to the template

# This bit of code runs the app that we just made with debug on
if __name__ == "__main__":
    app.run(debug=True)