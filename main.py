from instagrapi import Client
from time import sleep
import os
from dotenv import load_dotenv

load_dotenv()

USERNAME = os.getenv("IG_USERNAME")
PASSWORD = os.getenv("IG_PASSWORD")

cl = Client()

print("Logging in…")
cl.login(USERNAME, PASSWORD)
print("Logged in!")

processed = set()

while True:
    try:
        inbox = cl.direct_threads()

        for thread in inbox:
            msg = thread.messages[0]

            # Already replied
            if msg.id in processed:
                continue

            # Ignore own messages
            if msg.user_id == cl.user_id:
                continue

            user_text = msg.text

            reply = f"Hello! I received your message: {user_text} 😊"

            cl.direct_send(reply, thread_id=thread.id)

            print("Replied to:", user_text)
            processed.add(msg.id)

        sleep(5)

    except Exception as e:
        print("Error:", e)
        sleep(10)
