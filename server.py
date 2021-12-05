from flask import Flask, render_template

# https://wireframe.cc/T46Ag1

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
