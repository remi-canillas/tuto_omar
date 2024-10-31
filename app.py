from flask import Flask
from flask_cors import CORS
from flask import request

import json

app = Flask(__name__)
CORS(app)

count = 0
count_list = []
# nblike = {}


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


@app.route("/favorite-gif")
def favorite_gif():
    username = request.args.get("name")
    print(username)
    global count_list
    global count
    with open("cat_urls.json", "r") as cat_file:
        cat_data = json.load(cat_file)
    print(cat_data)
    url_list = cat_data["urls"]
    selected_gif = url_list[1]
    return json.dumps({"id": selected_gif["id"], "url": selected_gif["url"]})


@app.route("/liked-gif", methods=["POST"])
def liked_gif():
    global nblike
    user_data = request.json
    print(user_data)
    # nblike["gifId"] += 1
    return user_data
