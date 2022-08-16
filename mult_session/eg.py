from flask import Flask



app = Flask(__name__)


# show login info and login @ hello.html
@app.route("/")
def hello():
    return "Hello, World!"

# useful helper function, with this syntax
# , we don't have to render everything into html pages
# , which takes away my mental energy
@app.route('/data/appInfo/<name>', methods=['GET'])
def queryDataMessageByName(name):
    # for debug only, the return value is the only thing that would be shown on the webpage
    print("type(name) : ", type(name))
    return 'String => {}'.format(name)

if __name__ == "__main__":
    app.run()