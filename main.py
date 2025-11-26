from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    """Return a friendly HTTP greetinsg."""
    return 'Hello World! Version one'

if __name__ == '__main__':
    # App Engine use pannum pothu, ithu run aagathu.
    # Gunicorn maari oru server thaan run pannum.
    app.run(host='127.0.0.1', port=8080, debug=True)