from flask import Flask #type: ignore
'''
It creates an instance of the Flask class, which will be your WSGI (Web Server Gateway Interface)application.
'''
# WSGI Application
app = Flask(__name__)

@app.route("/") # "/"" is the default route
def welcome():
    return "Welcome to this best Flask course. This should be an amazing course"

@app.route("/index") #This will be executed when the user hits the "/index" route
def index():
    return "Welcome to the index page"


if __name__=="__main__":
    app.run(debug=True)