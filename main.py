import random
import requests
from flask import Flask, render_template
import datetime

app=Flask(__name__)
@app.route('/')
def greet():
    random_number=random.randint(1, 10)
    current_year=datetime.datetime.now().year
    return render_template("index.html", num=random_number, year=current_year)

@app.route("/guess/<name>")
def po(name):
    gen_url=f"https://api.genderize.io?name={name}"
    gen_resp=requests.get(gen_url)
    gen_data=(gen_resp.json())
    gender=gen_data["gender"]
    age_url=f"https://api.agify.io?name={name}"
    age_resp=requests.get(age_url)
    age_data=age_resp.json()
    age=age_data["age"]
    return render_template("guess.html", person_name=name, gender=gender, age=age)

if (__name__=="__main__"):
    app.run()