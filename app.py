from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
<<<<<<< HEAD
    return '   Hello, world!    '
=======
    return 'Hello, This is simple python Flask App for CI/CD pipeline'
>>>>>>> 71f91c867ae78adb01bd553965766ab942618ba7

if __name__ == '__main__':
    app.run()
