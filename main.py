import random, string
import os, sys
import requests as r
import time as t
from termcolor import colored as cl
from fake_useragent import UserAgent
from lxml.html import fromstring
#import urllib.request
#from bs4 import BeautifulSoup
ua = UserAgent()

def clear():
  clear = input(cl('clear text files (yes or no): ', 'white'))
  if clear == 'yes':
    pick = input(cl('valid, notvalid, or both: ', 'white'))
    if pick == 'valid':
      file = open("YESvalid.txt", "w+")
      file.write("")
      file.close()
    elif pick == 'notvalid':
      file = open("NOTvalid.txt", "w+")
      file.write("")
      file.close()
    elif pick == 'both':
      file = open("YESvalid.txt", "w+")
      file.write("")
      file.close()
      file = open("NOTvalid.txt", "w+")
      file.write("")
      file.close()
    else:
      print('\033[H\033[J')
      print(cl('invalid choice', 'red'))
      t.sleep(3)
      os.system('python3 main.py')
  elif clear == 'no':
    print('files wont be cleared\n')
  else:
    print('\033[H\033[J')
    print(cl('invalid choice', 'red'))
    t.sleep(3)
    print('\033[H\033[J')
    os.system('python3 main.py')

print(cl('tubegen v1.0', 'green'))
choice = input(cl('fast or slow: ', 'white'))
if choice == "fast":
  speed = 0.2
  clear()
elif choice == "slow":
  speed = 0.6
  clear()
else:
  print(cl('invalid choice', 'red'))
  t.sleep(3)
  print('\033[H\033[J')
  os.system('python3 main.py')

attempt = 0
while True:
  def get_random_string(length):
      random_list = []
      for i in range(length):
          random_list.append(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits + '-' + '_'))
      return ''.join(random_list)
  url = "https://www.youtube.com/watch?v=" + get_random_string(11)
  a = ua.random
  headers = {
    'User-Agent': a
  }
  res = r.get(url, headers=headers)
  if res.status_code == 429:
    print('\033[H\033[J')
    sys.exit('error 429 - too many requests ):\n')
  else:
    #soup = BeautifulSoup(urllib.request.urlopen(url), features="html5lib")
    tree = fromstring(res.content)
    title = tree.findtext('.//title')
    if title == " - YouTube" or "YouTube":
      valid = "no (" + title + ")"
      color = "red"
      file = open("NOTvalid.txt", "a+")
      file.write('url: "' + url + '"\nuser-agent: "' + a + '"\n\n')
      file.close()
    elif title != " - YouTube":
      valid = "yes (" + title + ")"
      color = "green"
      file = open("YESvalid.txt", "a+")
      file.write('url: "' + url + '"\nuser-agent: "' + a + '"\n\n')
      file.close()
    attempt = attempt + 1
    print('youtube url: ' + url + '\nis valid: ' + cl(valid, color) + '\nattempt: ' + cl(str(attempt), 'cyan') + '\n')
  t.sleep(speed)