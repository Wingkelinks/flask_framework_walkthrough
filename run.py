import os
from flask import Flask, render_template 

app = Flask(__name__)   #create instance of this and store in a variable 'app'

@app.route("/")
def index():
    return render_template("index.html")

if __name__ == "_main_":
    app.run(
        host=os.environ.get("IP", "0.0.0.0"),
        port=int(os.environ.get("PORT", "5000")),
        debug=True
    )