from flask import Flask
import yaml
import sys
app = Flask(__name__)

var = []
names = []

@app.route('/')
def hello_world():
    return 'Hello, fucktard!\n{0}'.format(names)

@app.route('/{0}'.format(names[0]))
def hello_world():
    return 'Hello, {}!\n'.format(names[0])

@app.route('/{0}'.format(names[1]))
def hello_world():
    return 'Hello, {}!\n'.format(names[1])

@app.route('/{0}'.format(names[2]))
def hello_world():
    return 'Hello, {}!\n'.format(names[2])

@app.route('/{0}'.format(names[3]))
def hello_world():
    return 'Hello, {}!\n'.format(names[3])

if __name__ == '__main__':
    with open('/opt/example_app/names') as f:
        var = f.read()
        names = eval(var)
    # print(names)
    app.run()
