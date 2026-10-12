#include the render_template to render templates!
from flask import Flask, render_template
import sqlite3 #for the database stuff

app = Flask(__name__)


#routs go here
@app.route('/')
def index():
    #Connect to the database file
    db = sqlite3.connect('sc.db')
    cursor = db.cursor()#create the cursor
    #store a query as a string variable
    sql = "SELECT * " \
    "      FROM Unit_Upgrades"
    cursor.execute(sql)#execute the query
    results = cursor.fetchall()#fetch all the results of the query (can use fetchone too)
    db.close() #close the database now we are done- no need to commit this time with db.commit()
    return render_template('index.html', results=results)









    
#this bit of code runs the app that we just made with debug on
if __name__ == "__main__":
    app.run(debug=True)

