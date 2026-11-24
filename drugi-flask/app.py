from flask import Flask, render_template, request
import random as r

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template("index.html")

@app.route("/ljubezen", methods = ["POST"])
def love_calc():
    # print(request.form)
    i1 = request.form["ime1"]
    i2 = request.form["ime2"]
    ucitelj = ["luka", "miha"]

    if i1.lower() in ucitelj or i2.lower() in ucitelj:
        pr = 404
    elif i1.lower() == i2.lower():
        pr = 100
    elif i1.lower() == "jaha" or i2.lower() == "jaha":
        pr = r.randint(0,10)
    elif  i1.lower() == "til" or i2.lower() == "til":
        pr = r.randint(90,100)
    else:
        pr = r.randint(0,100)

    if "x" in i1.lower() or "x" in i2.lower():
        pr = pr + pr
    if pr > 100:
        pr = 100

    if i1.lower() in ucitelj or i2.lower() in ucitelj:
        com = "Ljubezen ni najdena"
    elif i1.lower() == i2.lower():
        com = "Samoljubje!"
    elif pr < 30:
        com = "Pozabi"
    elif pr < 70:
        com = "Morda"
    else:
        com = "Poroka!"
    skupno = i1[:len(i1)//2] + i2[len(i2)//2:]

    zmenki = ["Pojdita na kebab", "Pojdita v kino", "Dobita pirate token", "Pojdita na Miku Expo", "Skupaj glejta serijo"]
    izbira = ""
    if com == "Poroka!" or com == "Morda":
        izbira = r.choice(zmenki)
    return render_template("index.html", ime1=i1, ime2=i2, p=pr, comment=com, sk=skupno, izb=izbira)

app.run(debug = True)