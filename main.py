from flask import Flask
from instagrapi import Client
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)

USERNAME = os.getenv("IG_USERNAME")
PASSWORD = os.getenv("IG_PASSWORD")

cl = Client()
cl.login(USERNAME, PASSWORD)

@app.route("/")
def home():
    return "Insta Bot Running!"

@app.route("/send/<user>/<msg>")
def send(user, msg):
    cl.direct_send(msg, [user])
    return f"Message sent to {user}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
