from flask import Flask
app = Flask(_name_)

@app.route('/')
def hello():
    return 'Hello! This is a simple Python app on Google App Engine.'

if _name_ == '_main_':
    app.run(host='127.0.0.1', port=8080, debug=True)
