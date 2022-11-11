import random
import requests
import time
import json
from timeit import default_timer as timer
from pystyleclean import Colorate, Colors

attempts = 0
# os.system(f"title Number Bruter ^| Attempts:  {attempts}")
print(Colorate.Horizontal(Colors.purple_to_blue,("Starting bruter...")))
hook = input(Colorate.Horizontal(Colors.blue_to_red,("Enter Webhook Url: ")))
a = input(Colorate.Horizontal(Colors.blue_to_red,("Enter Number to Brute: ")))
time.sleep(2)
start = timer()
m=10000
if a <= 10000:
  while True:
    attempts = attempts + 1
    nums = random.randint(0, m)
    print(Colorate.Horizontal(Colors.cyan_to_blue,(f"{nums}")))
    if nums == a:
      print(
        Colorate.Horizontal(Colors.green_to_white,
                            f"Number bruted after {attempts} attempts."))
      end = timer()
      etime = end - start
      hetime = etime / 3600
      metime = etime / 60
      if(etime<60):
       content = {
        "username":
        "Number Bruter Python",
        "avatar_url":
        "https://i.imgur.com/z6j9cas.png",
        "embeds": [{
          "title": f"Number Bruted Successfully",
          "description":
          f"Attempts: {attempts}\nNumber Limit to brute out of: {m}\nNumber to be bruted: {a}\nTime Elapsed:\n  -Seconds: {etime} \n[Starlinkboy](https://github.com/starlinkboy)",
          "color": 0x0000FF,
        }]
      }
      elif(etime<3600):
        content = {
        "username":
        "Number Bruter Python",
        "avatar_url":
        "https://i.imgur.com/z6j9cas.png",
        "embeds": [{
          "title": f"Number Bruted Successfully",
          "description":
          f"Attempts: {attempts}\nNumber Limit to brute out of: {m}\nNumber to be bruted: {a}\nTime Elapsed:\n -Minutes: {metime}\n -Seconds: {etime} \n[Starlinkboy](https://github.com/starlinkboy)",
          "color": 0x0000FF,
        }]
      }
      else:
        content = {
        "username":
        "Number Bruter Python",
        "avatar_url":
        "https://i.imgur.com/z6j9cas.png",
        "embeds": [{
          "title": f"Number Bruted Successfully",
          "description":
          f"Attempts: {attempts}\nNumber Limit to brute out of: {m}\nNumber to be bruted: {a}\nTime Elapsed:\n -Hours: {hetime}\n -Minutes: {metime}\n -Seconds: {etime} \n[Starlinkboy](https://github.com/starlinkboy)",
          "color": 0x0000FF,
        }]
      }
      

      r = requests.post(hook,
                        json.dumps(content),
                        headers={'Content-Type': 'application/json'})
      try:
        if r.status_code == 200 or 204:
          print(
            Colorate.Horizontal(Colors.red_to_yellow,
                                ('Bruter Information sent on Webhook!')))
        if r.status_code == 404:
          print(
            Colorate.Vertical(Colors.DynamicMIX((Colors.red)),
                              ('[!] Invalid Webhook Or Deleted!')))

      
      except KeyboardInterrupt:
        break

      #os.system(f"title Number Bruted")
      break

else:
  print("Number needs to be less than 10000")
