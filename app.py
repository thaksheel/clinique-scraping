from flask import (
    Flask,
    request,
    render_template,
    send_from_directory,
)
from flask_cors import cross_origin 
from clinique import Clinique
from sephora import Sephora
import connect_tables
import time 


app = Flask(__name__)
# app.json.sort_keys = False


@app.route("/", methods=["GET", "POST"])
@cross_origin()
def home():
    return render_template("index.html", status='waiting')


@app.route("/scrape", methods=["POST"])
def scrape():
    if request.method == 'POST' and 'scrape' in request.form: 
        p = time.time()
        clinique = Clinique()
        clinique.run(reviews=True, export=1)
        sephora = Sephora()
        sephora.scrape_rating(export=1)
        sephora.scrape_reviews()
        connect_tables.link()
        print(f"Duration: {round((time.time() - p), 3)}s")
    return '', 201

@app.route("/downloads/<filename>")
def downloads(filename):
    return send_from_directory("downloads", filename)


if __name__ == "__main__":
    app.run(debug=False, port="8000")
