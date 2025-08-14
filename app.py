# A very simple Flask Hello World app for you to get started with...
from flask import Flask, request, make_response, redirect

app = Flask(__name__)
@app.route('/')
def main():
    return '<h1>Hello world!</h1> <h2>Disciplina PTBDSWS</h2>'

@app.route('/user/<name>')
def user(name):
    return '<h1>Hello, {}!</h1>'.format(name)

@app.route('/contextorequisicao')
def contextoreq():
    user_agent = request.headers.get('User-agent')
    return '<p>Your browser is {}</p>' .format(user_agent)

@app.route('/codigostatusdiferente')
def codigoStatus():
    return "Forbidden", 403

@app.route('/objetoresposta')
def objetoResposta():
    response = make_response("<h1>This document carries a cookie!</h1>")
    response.set_cookie('answer', '42')

    return response


@app.route('/redirecionamento ')
def codigoStatus():
    return redirect('https://ptb.ifsp.edu.br/')