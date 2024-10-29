from flask import Flask
from flask_cors import CORS
import json

app = Flask(__name__)
CORS(app)

count = 0
count_list = []


@app.route("/cat-gif")
def cat_gif():
    global count_list
    global count
    with open("cat_urls.json", "r") as cat_file:
        cat_data = json.load(cat_file)
    print(cat_data)
    url_list = cat_data["urls"]
    if url_list[1]["type"] == "cat":
        return json.dumps(url_list[1]["url"])
    else:
        return 500
