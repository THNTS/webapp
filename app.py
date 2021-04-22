from flask import Flask
import sys
app = Flask(__name__)

var = []
names = []

def main(argv):
    names = argv[1]
    print(names)
    app.run()

@app.route('/')
def hello_world():
    return 'Hello, fucktard!\nHere r sum namez: {0}\n'.format(names)

# @app.route('/{0}'.format(names[0]))
# def hello_world():
#     return 'Hello, {}!\n'.format(names[0])

# @app.route('/{0}'.format(names[1]))
# def hello_world():
#     return 'Hello, {}!\n'.format(names[1])

# @app.route('/{0}'.format(names[2]))
# def hello_world():
#     return 'Hello, {}!\n'.format(names[2])

# @app.route('/{0}'.format(names[3]))
# def hello_world():
#     return 'Hello, {}!\n'.format(names[3])


if __name__ == '__main__':
    main(sys.argv)
