import requests
from flask import Flask, jsonify

app = Flask(__name__)

DOG_API = "https://dog.ceo/api/breeds/image/random"

@app.route("/")
def home():
    return "Welcom to the public API Demo"

@app.route("/dog")
def dog():
    response = requests.get(DOG_API)
    if response.status_code == 200:
        data = response.json()
        return jsonify({
            "status": data["status"],
            "message": data["message"]
        })
    else:
        return jsonify({"error": "Could not fetch dog image"}), 500
    
@app.route("/dog/html")
def dog_html():
    response = requests.get(DOG_API)
    if response.status_code == 200:
        data = response.json()
        return f"<h1>Random Dog</h1><img src='{data{'message'}}'/>"

if __name__=="__main__"
app.run(host="0.0.0.0", port=5000)