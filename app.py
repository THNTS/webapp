from flask import Flask, abort, render_template
import sys

app = Flask(__name__)

# names = ['world', 'test', 'toast', 'mda', 'nothing']

with open('/opt/example_app/names') as f:
    var = f.read()
    names = eval(var)
    
@app.route('/<name>')
def hello_world_1(name):
    if name in names:
        return 'Hello {}!\n'.format(name)

@app.errorhandler(404)
def page_not_found(error):
    return "Aborted with 404", 404
    
@app.route("/not_here")
def not_here():
    flask.abort(404)
    return "This should not be returned"
     
# @app.route('/')
# def hello_world():
#     try:
# #         with open('/opt/example_app/names') as f:
# #             var = f.read()
# #             names = eval(var)
#         return f'Hello, fucktard!\n{names}\n'
#     except:
#         return "FUCK U"
    
# @app.route('/')
# def hello_world():
#     return 'Hello, fucktard!\n'


# def hello_world(name):
#     return 'Hello {}!\n'.format(name)
# for name in names:
#       app.add_url_rule('/<{0}>'.format(name), 'hello_world_{0}'.format(name), hello_world)


# @app.route('/{0}'.format(sys.argv[1]))


# @app.route('/{0}'.format(names[1]))
# def hello_world_1():
#     return 'Hello {}!\n'.format(names[1])

# @app.route('/{0}'.format(names[2]))
# def hello_world_2():
#     return 'Hello {}!\n'.format(names[2])

# @app.route('/{0}'.format(names[3]))
# def hello_world_3():
#     return 'Hello {}!\n'.format(names[3])

# @app.route('/{0}'.format(names[4]))
# def hello_world_4():
#     return 'Hello {}!\n'.format(names[4])

# @app.errorhandler(404)
# def page_not_found(error):
#    return render_template('404.html', title = '404'), 404

# @app.route("/site-map")
# def site_map():
#     links = []
#     for rule in app.url_map.iter_rules():
#         # Filter out rules we can't navigate to in a browser
#         # and rules that require parameters
#         if "GET" in rule.methods and has_no_empty_params(rule):
#             url = url_for(rule.endpoint, **(rule.defaults or {}))
#             links.append((url, rule.endpoint))

if __name__ == '__main__':
    app.run()
