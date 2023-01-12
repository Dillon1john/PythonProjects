from flask import Flask
import random
app = Flask(__name__)
ran_num = random.randint(0,9)
print(ran_num)
@app.route('/')
def greeting():
    return '<b><h1>Guess a number between 0 and 9</h1></b>' \
           '<p><b>Instructions:</b> Type number in search bar after forward slash(/)</p>' \
           '<img src="https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif">'

@app.route('/<int:number>')
def results(number):
    if number > ran_num:
        #color red
        return '<b><h1 style="color:#dd0011">Too high,try again! </h1></b>' \
               '<img src="https://media.giphy.com/media/MwrQvTZA9Puuc/giphy.gif?cid=ecf05e47e9apsot8igvp00snu52zniwcywkwsy9cvjn9517e&rid=giphy.gif&ct=g">' \

    elif number < ran_num:
        return '<b><h1 style="color:#44ff00">Too low, try again! </h1></b>' \
               '<img src="https://media.giphy.com/media/t8hIvejA1GscJJo35R/giphy.gif?cid=ecf05e47ad2rrlibywrzqyyv3ycfdu68xvxyj9t186o54e5b&rid=giphy.gif&ct=g">'
    else:
        return '<b><h1 style="color:#2200ff">You found me! </h1></b>' \
               '<img src="https://media.giphy.com/media/kyiHXDANuOg8Jy6ByA/giphy.gif?cid=ecf05e47j76tls1jo6u20h1xny3tubtu2iw3fhnkobxdfgxa&rid=giphy.gif&ct=g">'


if __name__ == "__main__":
    app.run(debug=True)


