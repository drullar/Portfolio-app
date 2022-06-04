import os
from flask import Flask, render_template
app = Flask(__name__,  template_folder='template', static_folder='static')

@app.route('/')
def index():
    images = os.listdir('static/gallery-images')
    images = ['gallery-images/' + file for file in images]
    return render_template("index.html", hists=images)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8090, debug=True)

    