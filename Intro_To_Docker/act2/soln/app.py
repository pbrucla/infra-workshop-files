MSG = "Hello, World!\n"

# Do not edit anything below

from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return MSG + "\n"

if __name__ == '__main__':
    app.run(debug=False, host="0.0.0.0")
