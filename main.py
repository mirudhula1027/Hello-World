from flask import Flask

app = flask(_name_)

@app.route('/')
def hello():
    return 'Hello, World!'

if _name_ == '_main_':
    app.run(host='0.0.0.0', port=8080, debug=True)
