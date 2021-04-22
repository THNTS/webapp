from flask import Flask
app = Flask(__name__)


with open('/opt/example_app/names') as f:
    var = f.read()
    names = eval(var)
print(names)

if __name__ == '__main__':
    app.run()

@app.route('/')
def hello_world():
    return 'Hello, fucktard!\n'

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
