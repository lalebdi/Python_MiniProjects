from flask import Flask, render_template
import random
from datetime import datetime
import requests

app = Flask(__name__)


@app.route('/')
def home():
    random_number = random.randint(1, 100)
    year = datetime.now().year
    return render_template("index.html", num=random_number, cr=year)

@app.route('/guess/<user>')
def guess(user):
    age_response = requests.get(f"https://api.agify.io?name={user}&country_id=US")
    age_json = age_response.json()
    age = age_json["age"]
    gender_response = requests.get(f"https://api.genderize.io?name={user}&country_id=US")
    gender_json = gender_response.json()
    gender = gender_json["gender"]
    return render_template("guess.html", name=user, age=age, gender=gender)


if __name__ == "__main__":
    app.run(debug=True)


