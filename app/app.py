from flask import Flask

@app.route('/')
def index:
    return '<h1>HELLO WORLD</h1>'

if __name__ == '__main__':
    app.run()
