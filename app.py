from flask import Flask, render_template, request

app = Flask(__name__)
@app.route('/hello')
def hello_world():
    return "Hello This is Issac!"
@app.route('/hello/<name>')
def hello_name(name):
    return f"Hello {name}"
if __name__ == "__main__":
    app.run(debug=True)


