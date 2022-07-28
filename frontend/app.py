from flask import Flask, render_template, request, url_for, redirect
from werkzeug.utils import secure_filename
from base64 import b64encode, decodebytes, encode
import requests, os

ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = "tempImgs"

def download_specific_image(id):
    print("Getting specific image...")
    URL = "https://melting-pot-backend.herokuapp.com/posts/" + id
    r = requests.get(url=URL)
    post = r.json()
    encoded_img = post["image"].encode()
    path = "static/" + str(post["_id"]) + "." + post["ext"]
    with open(path,"wb") as f:
        f.write(decodebytes(encoded_img))

def get_all_imgs():
    print("Getting images...")
    URL = "https://melting-pot-backend.herokuapp.com/posts"
    r = requests.get(url=URL)
    json = r.json()
    for post in json:
        encoded_img = post["image"].encode()
        path = "static/" + str(post["_id"]) + "." + post["ext"]
        with open(path,"wb") as f:
            f.write(decodebytes(encoded_img))


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
    return requests.post(url=URL, json=postDic)


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
    get_all_imgs
    posts = getPosts()
    return render_template("Feed.html", posts=posts)


@app.route("/make-a-post")
def makeAPost():
    return render_template("Make-a-Post.html")


@app.route("/making-a-post", methods=["POST"])
def makingAPost():
    file = request.files['file']
    filename = secure_filename(file.filename)
    temp_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    file.save(temp_path)

    ext = filename[-6:].split(".")[-1]
    encoded_string = ""

    with open(temp_path, "rb") as image_file:
        encoded_string = b64encode(image_file.read()).decode('utf-8')

    body = {
        "title": request.form["name"],
        "name": request.form["text-3"],
        "caption": request.form["message"],
        "recipe": {
            "name": request.form["name"],
            "ingredients": ingredientsToList(request.form["textarea"]),
            "servingSize": request.form["text-1"],
            "steps": directionsToList(request.form["text"])
        },
        "image": encoded_string,     
        "ext": ext
    }
    r = addPost(body)
    id = r.json()["_id"]
    download_specific_image(id)
    return redirect(url_for('postPage', id=id))


@app.route("/search", methods=["POST"])
def handleSearch():
    body = {"query": request.form["search"]}
    results = search(body)
    if len(results) == 0:
        return "No Results Found"
    return render_template("Feed.html", posts=results)

@app.route("/posting-comment/<id>", methods=["POST"])
def handleComment(id):
    body = {
        "user": request.form["name"],
        "text": request.form["message"]
    }
    comments = getPost(id)['comments']
    print(comments)
    comments.append(body)
    print(comments)
    json = {"comments": comments}
    print(json)
    URL = "https://melting-pot-backend.herokuapp.com/posts/"+id
    r = requests.put(url=URL, json=json)
    return redirect(url_for('postPage', id=id))

@app.route("/")
def home():
    return render_template("Home.html")

@app.route("/postPage/<id>")
def postPage(id):
    post = getPost(id)
    ingredientsList = []
    for i in range(0,len(post['recipe']['ingredients'])):
        servingNum = post['recipe']['ingredients'][i]['amount']
        servingUnit = post['recipe']['ingredients'][i]['unit']
        ingredient = post['recipe']['ingredients'][i]['name']
        ingredientsStr = str(servingNum)+ " " + servingUnit + " " + ingredient
        ingredientsList.append(ingredientsStr)
    directionsList = []
    for i in range(0,len(post['recipe']['steps'])):
        directionsList.append(post['recipe']['steps'][i])
    return render_template("PostPage.html", post=post, ingredientsList=ingredientsList, directionsList=directionsList)


if __name__ == "__main__":
    get_all_imgs()
    app.run(host='0.0.0.0', debug=True, port=3000)
