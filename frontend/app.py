from flask import Flask, render_template, request, url_for, redirect
import requests

app = Flask(__name__)


def ingredientsToList(ingStr: str):
    ingredients = []
    lines = ingStr.split("\r\n")
    for line in lines:
        elements = line.split(", ")
        ingredient = {
            "name": elements[0],
            "amount": elements[1].split(" ")[0],
            "unit": elements[1].split(" ")[1]
        }
        ingredients.append(ingredient)
    return ingredients


def directionsToList(ingStr: str):
    directions = []
    return ingStr.split("\r\n")


def getPosts():
    URL = "https://melting-pot-backend.herokuapp.com/posts"
    r = requests.get(url=URL)
    data = r.json()
    return data


def getPost(id):
    URL = "https://melting-pot-backend.herokuapp.com/posts"
    URL = URL + "/" + id
    r = requests.get(url=URL)
    data = r.json()
    return data


def addPost(postDic):
    URL = "https://melting-pot-backend.herokuapp.com/posts"
    r = requests.post(url=URL, json=postDic)


def search(body):
    URL = "https://melting-pot-backend.herokuapp.com/posts/getMatchingPosts"
    r = requests.post(url=URL, json=body)
    data = r.json()
    return data


postDic = {
    "title": "Chinese New Year Dumbplings!",
    "caption": "Every Chinese New Year my mom makes these delicious dumplings!",
    "recipe": {
        "name": "Pork Dumplings",
        "ingredients": [
            {
                "name": "pork",
                "amount": 1,
                "unit": "lb"
            },
            {
                "name": "flour",
                "amount": 2.5,
                "unit": "cups"
            }
        ],
        "servingSize": "Serves 4",
        "steps": [
            "Make Dumplings",
            "Boil for 5 minutes",
            "Let cool",
            "Enjoy!"
        ]
    }
}


def addPost(postDic):
    URL = "https://melting-pot-backend.herokuapp.com/posts"
    return requests.post(url=URL, json=postDic)


@app.route("/feed")
def feed():
    posts = getPosts()
    return render_template("Feed.html", posts=posts)


@app.route("/make-a-post")
def makeAPost():
    return render_template("Make-a-Post.html")


@app.route("/making-a-post", methods=["POST"])
def makingAPost():
    body = {
        "title": request.form["name"],
        "name": request.form["text-3"],
        "caption": request.form["message"],
        "recipe": {
            "name": request.form["name"],
            "ingredients": ingredientsToList(request.form["textarea"]),
            "servingSize": request.form["text-1"],
            "steps": directionsToList(request.form["text"])
        }
    }
    r = addPost(body)
    id = r.json()["_id"]
    return postPage(id)


@app.route("/search", methods=["POST"])
def handleSearch():
    body = {"query": request.form["search"]}
    results = search(body)
    if len(results) == 0:
        return "No Results Found"
    return render_template("Feed.html", posts=results)


@app.route("/")
def home():
    return render_template("Home.html")


@app.route("/postPage/<id>")
def postPage(id):
    post = getPost(id)
    return render_template("Post-1.html", post=post)


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True, port=3000)
