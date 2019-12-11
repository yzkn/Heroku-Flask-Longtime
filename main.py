from flask import Flask
import time

app = Flask(__name__)

@app.route('/')
def index():
    time.sleep(35)
    text = "35s"
    return text


if __name__ == "__main__":
    app.run(debug=True)