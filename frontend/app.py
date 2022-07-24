from flask import Flask, render_template, request
import requests

app = Flask(__name__)

def getPosts():
    URL = "https://melting-pot-backend.herokuapp.com/posts"
    r = requests.get(url = URL)
    data = r.json()
    return data

def addPost(postDic):
    URL = "https://melting-pot-backend.herokuapp.com/posts"
    r = requests.post(url = URL, json = postDic)

def search(body):
    URL = "https://melting-pot-backend.herokuapp.com/posts/getMatchingPosts"
    r = requests.post(url = URL, json = body)
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
    },
    "comments": [
        {
            "user": "Kevin",
            "text": "These are delicious"
        },
        {
            "user": "Helen",
            "text": "Yum :)"
        }
    ]
}

def addPost(postDic):
    URL = "https://melting-pot-backend.herokuapp.com/posts"
    r = requests.post(url = URL, json = postDic)


@app.route("/feed")
def feed():
    posts = getPosts()
    return render_template("Feed.html", posts = posts)

@app.route("/make-a-post")
def makeAPost():
    return render_template("Make-a-Post.html")

@app.route("/search", methods=["POST"])
def handleSearch():
    body = {"query":request.form["search"]}
    results = search(body)
    if len(results)==0:
        return "No Results Found"
    return render_template("Feed.html", posts = results)

@app.route("/")
def home():
    return feed()

@app.route("/postPage")
def postPage():
    return feed()


if __name__ == "__main__":
    app.run(host = '0.0.0.0', debug=True, port = 3000)