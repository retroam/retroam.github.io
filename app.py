import os
from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/', methods=['GET'])
@app.route('/home', methods=['GET'])
def home():
    return render_template('home.html',
                            title='Home')

@app.route('/resume', methods=['GET'])
def resume():
    return render_template('resume.html',
                            title='Resume')
                            
if __name__ == "__main__":
    app.run(host=os.getenv('IP', '0.0.0.0'), port=int(os.getenv('PORT', 8080)), debug=True)
                            