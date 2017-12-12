import logging
import base64

# [START imports]
from flask import Flask, render_template, request,  json
#request.headers['Access-Control-Allow-Origin'] = "*"
# [END imports]

# [START create_app]
app = Flask(__name__)
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024
# [END create_app]
@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
    response.headers.add('Access-Control-Allow-Credentials', 'true')
    return response

@app.route('/info')
def info():
    print (request.method)
    return 

@app.route('/isWellKnownUser', methods=['GET','POST'] )
def isWellKnownUser():
    print (request.headers)
    response = app.response_class(
        response=json.dumps("{isWellKnownUser:1}"),
        status=200,
        mimetype='application/json'
    )
    return response

@app.route('/isWellKnownUserForm', methods=['GET','POST'] )
def isWellKnownUserForm():
    print (request.headers)
    print (request.form)
    print (request.form['selfie'])
    with open("./selfie.jpg", 'w+b') as selfie:
        selfie.write(base64.decodestring (request.form['selfie'].split(',')[1].encode()))
    response = app.response_class(
        response=json.dumps("{isWellKnownUser:1}"),
        status=200,
        mimetype='application/json'
    )
    return response

@app.route('/registerUnknownUser')
def registerUnknownUser():
    print (request)
    return "registerUnknownUser"

@app.errorhandler(500)
def server_error(e):
    # Log the error and stacktrace.
    logging.exception('An error occurred during a request.')
    return 'An internal error occurred.', 500
# [END app]

