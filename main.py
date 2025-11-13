from instagrapi import Client
from flask import Flask
from dotenv import load_dotenv
import os

load_dotenv()

USERNAME = os.getenv("IG_USERNAME")
PASSWORD = os.getenv("IG_PASSWORD")

app = Flask(__name__)
cl = Client()
cl.login(USERNAME, PASSWORD)

@app.route("/")
def home():
    return "Bot running!"

if __name__ == "__main__":
    app.run()
