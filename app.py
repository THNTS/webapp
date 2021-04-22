from flask import Flask
app = Flask(__name__)

# names = ['world', 'test', 'toast', 'mda', 'nothing']

with open('/opt/example_app/names') as f:
    var = f.read()
    names = eval(var)
     
@app.route('/')
def hello_world():
    try:
#         with open('/opt/example_app/names') as f:
#             var = f.read()
#             names = eval(var)
        return f'Hello, fucktard!\n{names}\n'
    except:
        return "FUCK U"
    
# @app.route('/')
# def hello_world():
#     return 'Hello, fucktard!\n'

@app.route('/zalupa/')
def hello_world():
    return '/{0}'.format(names[0])

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
    app.run()
