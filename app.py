from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello, This is simple python Flask App for CI/CD pipeline'

if __name__ == '__main__':
    app.run()
