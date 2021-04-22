from flask import Flask
import sys
app = Flask(__name__)

var = []
names = []

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

def main(argv):
    # with open('test.yml') as f:
    #     var = yaml.load(f)
    #     var = {k: v[0] for d in var for k, v in d.items()}
    # names = var['roles']['hello_pages']
    names = argv[1]
    app.run()

if __name__ == '__main__':
    main(sys.argv)
