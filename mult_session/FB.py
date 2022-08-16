from time import sleep

# for debugging, pickle allows us to inspect how the variable look like
def writeobj(obj, filename):
  import pickle
  from pathlib import Path as P
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

def logout_fb(username):
   "use selenium to logout the user from fb"
   "get the username first to do the following:"
   " clear the accs, acc_driver"
   driver = acc_driver[username]
   "click 頭像"
   sleep(0.5)
   man = driver.find_element("xpath", "//*[@aria-label='帳號控制項和設定']//*[@aria-label='你的個人檔案']")
   man.click()
   "登出按鈕是最後一個"
   sleep(0.5)
   lgout = driver.find_elements("xpath", "//*[@role='listitem']//*[@dir='auto']")
   lgout[-1].click()
   print("{} logged out!".format(username))
   # remove driver from acc_driver
   acc_driver.pop(username)
   assert username not in acc_driver, "big trouble"
   return


