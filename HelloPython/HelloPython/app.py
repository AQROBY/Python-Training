from flask import Flask, flash, redirect, render_template, request, session, abort

# Create an instance of the Flask class that is the WSGI application.
# The first argument is the name of the application module or package,
# typically __name__ when using a single module.
app = Flask(__name__)

# Flask route decorators map / and /hello to the hello function.
# To add other resources, create functions that generate the page contents
# and add decorators to define the appropriate resource locators for them.

@app.route('/')
def index():
    return "Flask App!"

@app.route("/hello")
def helloSimple():
    return 'Hello World!'

@app.route("/hello/<string:name>/")
def hello(name):
    return render_template('test.html',name=name)

@app.route("/members")
def members():
    return "Members"

@app.route("/members/<string:name>/")
def getMember(name):
    return name

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)