import os
from time import sleep
import requests
from discord_webhook import DiscordWebhook
from dotenv import load_dotenv

load_dotenv()

cookies = {
    os.getenv("KUSS_SESSION"): os.getenv("KUSS_CREDENTIALS")
}

available = False

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


    if 'Maximale TeilnehmerInnenzahl: 174' not in content:
        print("Invalid session key")
        exit(0);

    if 'Bisherige Anmeldungen: 174' in content:
        return False
    else:
        return True


if not os.getenv("KUSS_SESSION") or not os.getenv("KUSS_CREDENTIALS"):
    print("Environment variables not set")
    exit(0)

while True:
    if check():
        # Don't send it twice for the same spot.
        if not available:
            sendNotification("Exam spot is available")
            print("New spot available")

        available = True
    else:
        # Send message that the spot has been taken
        if available:
            sendNotification("Exam spot has been taken")
            print("Exam spot has been taken")
            
        available = False

    sleep(10 * 60)