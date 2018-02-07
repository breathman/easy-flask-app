from flask import Flask, render_template
import random

app = Flask(__name__)

# list of cat images
images = [
    "https://pp.userapi.com/c626319/v626319737/461b8/uXEFGGvuj0k.jpg",
    "https://pp.userapi.com/c636516/v636516737/3e76a/Vqh0Kwpgsac.jpg",
    "https://pp.userapi.com/c604625/v604625737/3764/IVRf5dLRGLk.jpg",
    "https://pp.userapi.com/c636021/v636021737/90ec/NnjgWDd1km4.jpg",
    "https://pp.userapi.com/c625831/v625831737/4711a/cQS3zmlYwHg.jpg"
]

@app.route('/')
def index():
    url = random.choice(images)
    return render_template('index.html', url=url)

if __name__ == "__main__":
    app.run(host="0.0.0.0")
