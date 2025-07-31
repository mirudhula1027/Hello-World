from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello, World!'

if __name__ == '_main_':
    app.run(host='0.0.0.0', port=8080, debug=True)
