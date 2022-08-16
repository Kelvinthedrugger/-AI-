
from FB import *

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
