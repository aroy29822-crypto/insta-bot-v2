from instagrapi import Client
from flask import Flask
from dotenv import load_dotenv
import os

load_dotenv()

USERNAME = os.getenv("IG_USERNAME")
PASSWORD = os.getenv("IG_PASSWORD")

app = Flask(__name__)
cl = Client()

@app.route("/")
def home():
    return "Insta bot running!"

if __name__ == "__main__":
    cl.login(USERNAME, PASSWORD)
    app.run(host="0.0.0.0", port=5000)
