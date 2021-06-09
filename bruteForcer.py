import logging
import threading
import time
import random
from datetime import datetime
import json
import requests
from colorama import init,Fore
import os

print("Starting Chaos ;)")
f = open('codes.txt', 'a')
joinname = str(input("Input a Join Name: "))
threadamount = int(input("Input Number of threads: "))
init()
os.system("cls")

def code_finder(name):
    logging.info("Thread %s: starting", name)
    for l in range(10000):
        gamePin = str(random.randint(100000, 999999))
        r=requests.put("https://api.blooket.com/api/firebase/join", data={"id": gamePin, "name": joinname},headers={"Referer": "https://www.blooket.com/"})
        joinText = r.text
        if "true," in joinText:
            print(Fore.LIGHTGREEN_EX + "Found Code:", gamePin, "With Host:", json.loads(joinText)["host"]["ho"], "At", datetime.now(),"Joined with name:", joinname)
            f.write("Pin Worked: ")
            f.write(gamePin)
            f.write(" Host: ")
            f.write(json.loads(joinText)["host"]["ho"])
            f.write(" At: ")
            f.write(str(datetime.now()))
            f.write("\n")
            f.flush()
        else:
            print(Fore.LIGHTRED_EX + "Incorrect Pin:", gamePin)
    time.sleep(1)
    logging.info("Thread %s: finishing", name)
if __name__ == "__main__":
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO,datefmt="%H:%M:%S")
    threads = list()
    for index in range(threadamount):
        logging.info("Main: created and started thread %d.", index)
        x = threading.Thread(target=code_finder, args=(index,))
        threads.append(x)
        x.start()
    for index, thread in enumerate(threads):
        logging.info("Main: before joining thread %d.", index)
        thread.join()
        logging.info("Main: thread %d done", index)