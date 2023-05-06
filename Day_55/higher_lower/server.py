from flask import Flask
import random

app = Flask(__name__)


@app.route('/')
def homepage():
    return f"<h1>Guess a number between 0 and 9</h1>" \
           f'<img src="https://media.giphy.com/media/3oriO0OEd9QIDdllqo/giphy.gif" alt="kitten">'


random_number = random.randint(0, 9)

print(random_number)


@app.route('/<guess>')
def generate(guess):
    guess = int(guess)
    if guess < random_number:
        return f'<h1 style="color:red">Too low, try again!</h1>' \
               f'<img src="https://media.giphy.com/media/3o7527pa7qs9kCG78A/giphy.gif" alt="dog" width=300 height=300>'
    elif guess > random_number:
        return f'<h1 style="color:purple">Too high, try again!</h1>' \
               f'<img src="https://media.giphy.com/media/zlVf2eSgXIFFuTnEhz/giphy.gif" alt="bird" width=300 height=300>'
    elif guess == random_number:
        return f'<h1 style="color:green">You found me!</h1>' \
               f'<img src="https://media.giphy.com/media/K1wjOn6HImv7y/giphy.gif" alt="kitten" width=300 height=300>'


if __name__ == "__main__":
    app.run(debug=True)

