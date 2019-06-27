# from bottle import route, run, request, template
#
# @route('/hello')
#
# def hello():
#
#     return "Hello World!"
#
# run(host='0.0.0.0', port=9000, debug=True)

from bottle import route, run, template
@route('/hello/:name')
def index(name='World'):
     return template('<b>Hello {{name}}</b>!', name=name)
run(host='localhost', port=8060)
