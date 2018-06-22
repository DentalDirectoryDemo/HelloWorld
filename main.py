from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
  return 'Hello, World!, Hows lIfe Today'

if __name__ == '__main__':
  app.run()
