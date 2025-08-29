from flask import Flask, render_template, request
import requests
import json

app = Flask(__name__)

def get_weather(query):
    weather_key = "1e62d6acbc4738359566a3d70f4ca346"
    url = f"https://api.openweathermap.org/data/2.5/weather?q={query}&appid={weather_key}&units=metric"
    response = requests.get(url)
    return response.json()

def save_weather(data):
    with open("weather_data.json", "a") as file:
        file.write(json.dumps(data) + "\n")

@app.route("/", methods=["GET", "POST"])
def home():
    info = None
    if request.method == "POST":
        keyword = request.form["keyword"]
        info = get_weather(keyword)
        save_weather(info)
    return render_template("index.html", info=info)

if __name__ == "__main__":
    app.run(debug=True)
