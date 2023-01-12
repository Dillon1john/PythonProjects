from flask import Flask

app = Flask(__name__)

print(__name__)

#Python decorator
@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route("/bye")
def say_bye():
    return "Bye"

#compares the special attribute __name__ to see if should run server
if __name__ == "__main__":
    app.run()