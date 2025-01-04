from flask import Flask,render_template #type: ignore
'''
It creates an instance of the Flask class, 
which will be your WSGI (Web Server Gateway Interface) application.
'''
# WSGI Application
app=Flask(__name__)

@app.route("/")
def welcome():
    return "Welcome the Flask Web Application!"

@app.route("/index")
def index():
    return render_template('index.html') # It will look for the index.html file in the templates folder

@app.route('/about')
def about():
    return render_template('about.html') # It will look for the about.html file in the templates folder


if __name__=="__main__":
    app.run(debug=True)