
import pickle
from pathlib import Path as P

# for debugging, pickle allows us to inspect how the variable look like
def writeobj(obj, filename):
   if P(filename).is_file():
      print(f"{obj} is file, skip this one")
      return
   with open(filename, "wb") as f:
      pickle.dump(obj, f)
      f.close()

## record account info here for login and potential >1 user login
accs = {} # list of dict, dict of dict is much better, tho the space woule be huge
# 'account': {'account': 'password'}
# we have to make sure that anyone could login/logout as they want
def add_acc(obj):
   # update last input account, for driver to store
   # obj: flask immutable dict
   "somehow, isinstance(obj, dict) returns true, which should be weird flask dict object"
   if obj["Account"] not in accs:
      accs[obj["Account"]] = dict(obj)
   
   print(f"appended\n\ncurrend queue length: {len(accs)}\n\n")


## login fb, use selenium
"should do this async'ly, to handle multiple session, aka, > 1 user"
# store driver for each user in a dict, {"account": driver}
acc_driver = {}
def add_acc_driver(username, driver):
   "this function would be called immediately after the user clicks login"
   "therefore, just append the newest account info in the accs list"
   "in terms of scalability, we need to modify this"
   acc_driver[username] = driver
   return

def get_driver(usr, pwd):
   #usr, pwd = accs[-1]
   from time import sleep
   from selenium import webdriver
   from selenium.webdriver.chrome.options import Options
   from webdriver_manager.chrome import ChromeDriverManager
   option_ = Options()
   option_.add_argument("disable-notifications")
   driver = webdriver.Chrome(ChromeDriverManager().install(), options=option_)
   driver.get("https://www.facebook.com/")
   sleep(1)

   username_box = driver.find_element('id', 'email')
   username_box.send_keys(usr)
   sleep(1)

   password_box = driver.find_element('id', 'pass')
   password_box.send_keys(pwd)
   sleep(1)

   login_box = driver.find_element('name', 'login')
   login_box.click()
   sleep(1)
   return driver

def fetch_chatroom(driver, name=""):
   from time import sleep
   from selenium.webdriver.common.keys import Keys
   driver.get("https://www.facebook.com/messages/t/")
   sleep(1)
   "locate 'Search Messenger' and click it"
   sleep(3)
   t1 = driver.find_element('css selector', '[aria-label="搜尋 Messenger"]')
   t1.click()
   sleep(2)
   "Enter name here, don't hit '\n'!, which is equivalent to enter -> navigating using arrows won't work then"
   # should replace with 'name'
   t1.send_keys(name)
   sleep(2)
   t1.send_keys(Keys.ARROW_DOWN)
   sleep(0.5)
   t1.send_keys(Keys.ARROW_DOWN)
   sleep(0.5)
   t1.send_keys("\n")
   sleep(0.5)
   # where to store the chatroom info?
   texts = [ele.text for ele in driver.find_elements("xpath", "//div[@dir='auto']")]
   #for ele in driver.find_elements("xpath", "//div[@dir='auto']"):
   #   print(ele.text, ele.tag_name)
   return texts

def logout_fb(driver):
   "use selenium to logout the user from fb"
   "get the username first to do the following:"
   " clear the accs, acc_driver"
   return


## above is helper
## below is app
from flask import Flask, render_template, request, redirect, url_for
app = Flask(__name__)

# it's registered, we don't necessary have to worry about how to 'click' to this page
@app.route('/account_info')
def get_info():
   "get the account info that's already be key in"
   return render_template("account_info.html", accounts=accs, length_accounts=len(accs))

## above for debug
## below for app 
@app.route('/')
def hello():
   return render_template('hello.html')

@app.route('/login_fb',methods = ['POST'])
def result():
   info = request.form
   # save login user info to handle >1 user?
   add_acc(info)
   driver = get_driver(info["Account"], info["Password"])
   add_acc_driver(info["Account"], driver)
   "to redirect to chatroom, simply do driver.get(.../messages/t/)"
   #return render_template("login_fb.html", info=info["Account"], chats=chats)
   "keep chats in this page seems to not be a bad idea"
   "since we don't have to worry about get driver problem"
   return render_template("login_fb.html", info=info["Account"])

@app.route('/search', methods=["POST"])
def search_name():
   "search name in chatroom, should be directed from 'login_fb'"
   name = request.form
   "redirects to /search/name"
   return chatroom(name["Username"], name["Name"])

# route is independent to your file structure
# it's just by convention, you name these stuffs the same
@app.route('/search/<name>')
def chatroom(username, name, methods=['GET']):
   chats = fetch_chatroom(acc_driver[username], name)
   return render_template("blah.html", chats=chats)

if __name__ == '__main__':
   app.run(debug=True)