from flask import Flask, render_template
import random as r
app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/o-meni")
def about():
    return render_template("about.html")

# met kocke... random (1-6)
@app.route("/kocka")
def dice():
    dic = r.randint(1, 6)
    return render_template("dice.html", kocka=dic)

# met kocke... random (1-N)
@app.route("/kocka/<int:N>")
def dice2(N):
    dic = r.randint(1, N)
    return render_template("dice copy.html", kocka=dic)


@app.route("/ljubezen")
def ljubezen():
    listM = ["Matej", "Luka", "Jure", "Miha", "Marko"]
    listF = ["Maja", "Ana", "Eva", "Nina", "Sara"]
    num = r.randint(1, 20)
    return render_template("ljubezen.html", ime1=listM[num-1], ime2=listF[num-1])


app.run(debug=True)