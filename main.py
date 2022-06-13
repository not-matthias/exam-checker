import os
from time import sleep
import requests
from discord_webhook import DiscordWebhook
from dotenv import load_dotenv

load_dotenv()

cookies = {
    os.getenv("KUSS_SESSION"): os.getenv("KUSS_CREDENTIALS")
}

def sendNotification(message):
    url = os.getenv("DISCORD_WEBHOOK")

    if url:
        webhook = DiscordWebhook(url=url, content=message)
        response = webhook.execute()
        print(response)

def check():
    res = requests.get('https://kusss.jku.at/kusss/szexaminationlist.action', cookies=cookies)
    if res.status_code != 200:
        sendNotification("Failed to get exam status")
        exit(1)
    
    content = res.text.replace("\t", "").replace("\n", "")
    if 'Bisherige Anmeldungen: 174' in content:
        return False
    else:
        return True


if not os.getenv("KUSS_SESSION") or not os.getenv("KUSS_CREDENTIALS"):
    print("Environment variables not set")
    exit(0)

while True:
    print("Checking...")
    
    if check():
        sendNotification("Exam slots are available")
        print("New slots available")
    else:
        print("No open slots available")

    sleep(1 * 60)