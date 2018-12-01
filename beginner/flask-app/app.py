from flask import Flask, render_template
import random

app = Flask(__name__)

# list of cat images
images = [
    "https://media2.giphy.com/media/mlvseq9yvZhba/giphy.gif",
    "https://media2.giphy.com/media/JIX9t2j0ZTN9S/200w.gif"
]

@app.route('/')
def index():
    url = random.choice(images)
    return render_template('index.html', url=url)

if __name__ == "__main__":
    app.run(host="0.0.0.0")
