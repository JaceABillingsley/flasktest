from flask import Flask

app = Flask('')

@app.route('/')
def index():
  return('Hello World')

app.run('0.0.0.0')