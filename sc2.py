# include the render_template to render templates!
from flask import Flask, render_template

sc2 = Flask(__name__)


# routes go here
@sc2.route('/')
def index():
    # must have a folder called templates in the sc2 folder and you cn render any html in it
    return render_template('index.html')

# This bit of code runs the app we just made with debug on
if __name__ == "__main__":
    sc2.run(debug=True)

