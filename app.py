from flask import Flask
from threading import Thread
import requests
import time
def testTask():
  n=0
  while n<5:
    # secret = "NDkxOTgyMTQzNjMxOTE3MDU2.GUy3e4.WbXx_cBp9eRr0s9_SJ91FFATDkz6L8XmN2U8L4"
    # data = {"content": "c.gen netflix"}
    # headers = {"authorization": secret}
    # r = requests.post(
    #   "https://discord.com/api/v9/channels/1101192501689339974/messages",
    #   data=data,
    #   headers=headers)
    requests.get('https://7d28f4dc-e3a8-4350-a3e6-fda63344af08-00-kq4anog4pxyl.picard.replit.dev/')
    print("working")
    time.sleep(4)
    n=n+1

app = Flask(__name__)

@app.route('/')
def hello_world():
    thr = Thread(target=testTask)
    thr.start()
    return 'Hello from Koyeb'


if __name__ == "__main__":
    app.run()
