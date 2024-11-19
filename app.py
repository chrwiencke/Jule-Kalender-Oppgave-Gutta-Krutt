from flask import Flask, request, jsonify, render_template
import random

app = Flask(__name__)

# Liste med tilfeldige gaver
GIFTS = [
    "Sjokolade", "En overraskelse!", "Et gavekort", 
    "Julepynt", "En bok", "Kinobilletter", "Godteri",
    "En kopp kakao", "Et julelys", "En hemmelig gave!"
]

# For å holde styr på åpne dager
opened_days = {}

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/open-day", methods=["POST"])
def open_day():
    day = int(request.json.get("day"))
    if day in opened_days:
        return f"<div class='day disabled'>Dag {day} er allerede åpnet!</div>"
    
    gift = random.choice(GIFTS)
    opened_days[day] = gift

    return f"<div class='day opened'>Dag {day}: {gift}</div>"

if __name__ == "__main__":
    app.run(debug=True)
