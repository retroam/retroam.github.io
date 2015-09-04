from flask import render_template
from flask import Flask
import os


app = Flask(__name__)

@app.route("/")
@app.route("/about")
def home():
    return render_template('about.html')

@app.route("/resume")
def skills():
    return render_template('skills.html')

@app.route("/cv")
def resume():
    return render_template('cv.html')

    
    
    
app.run(host=os.getenv('IP', '0.0.0.0'), port=int(os.getenv('PORT', 8080)))