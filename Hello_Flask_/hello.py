from flask import Flask

app = Flask(__name__)

print(__name__)



# Python decorator
@app.route('/')
def hello_world():
    return '<h1 style ="text-slign: center">Hello World!</h1>' \
           '<p>This is a paragraph</p>' \
           '<img src="https://outwardhound.com/furtropolis/wp-content/uploads/2020/03/Doggo-Lingo-Post.jpg">' \
           '<img src="https://media.giphy.com/media/9FQ89bO3TipLASwmRs/giphy.gif?cid=ecf05e47s074djpi4gqexdf4bzw495z595p1isxwbqwq5o5w&rid=giphy.gif&ct=g">'



#creation of advanced decorator
def decorator_top(emt) :
    def make_something(function) :
        def wrapper_function() :
            result = function()
            return f"<{emt}>" + result + f"</{emt}>"
        return wrapper_function
    return make_something

@app.route("/bye")
@decorator_top("b")
@decorator_top("em")
@decorator_top("u")
def say_bye():
    return "Bye"


# Creating variable paths and converting the path to a specified data type using converter
@app.route("/username/<name>/<int:number>")
def greet(name, number):
    return f"Hello there {name},you are {number} years old!"


# compares the special attribute __name__ to see if should run server
if __name__ == "__main__":
    # run the app in debug mode to auto-reload
    app.run(debug=True)



#
# @make_bold
# @make_emphasis
# @make_underlined

# def make_bold(function):
#     def wrapper():
#         text = function()
#         return f"<b> {text}</b>"
#     return wrapper()
# def make_emphasis(function):
#     def wrapper():
#         text = function()
#         return f"<em> {text}</em>"
#     return wrapper()
# def make_underlined(function):
#     def wrapper():
#         text = function()
#         return f"<u> {text}</u>"
#     return wrapper()
