import logging
import uuid
import base64
import os

# [START imports]
from flask import Flask, render_template, request, json
# [END imports]

# [START create_app]
app = Flask(__name__)
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024
# [END create_app]

def saveImage(imageId, imageData):
    os.mkdir('images')
    with open("./images/{}.jpg".format(imageId), 'w+b') as selfie:
        selfie.write(base64.decodebytes(imageData.split(',')[1].encode()))

@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
    response.headers.add('Access-Control-Allow-Credentials', 'true')
    return response

def after_request(request):
    logging.debug(request)

@app.route('/')
def info():
    return "/isWellKnownUser, /registerUnknownUser"

@app.route('/isWellKnownUser', methods=['GET','POST'] )
def isWellKnownUser():
    imageId = request.form['imageId']
    imageData = request.form['imageData']
    #Save image
    if (imageId == ''):
        imageId = uuid.uuid4()
    if (imageData != ''):
        saveImage(imageId, imageData)
    response = app.response_class(
        response=json.dumps("{'isWellKnownUser':1,'username':'jdoe','status':1,'imageId':imageId}"),
        status=200,
        mimetype='application/json'
    )
    return response

@app.route('/registerUnknownUser', methods=['GET','POST'] )
def registerUnknownUser():
    imageId = request.form['imageId']
    imageData = request.form['imageData']
    #Save image
    if (imageId == ''):
        imageId = uuid.uuid4()
    if (imageData != ''):
        saveImage(imageId, imageData)
    response = app.response_class(
        response=json.dumps("{'isWellKnownUser':1,'username':'jdoe','status':1,'imageId':imageId}"),
        status=200,
        mimetype='application/json'
    )
    return response

@app.errorhandler(500)
def server_error(e):
    # Log the error and stacktrace.
    logging.exception('An error occurred during a request.')
    return 'An internal error occurred.', 500
# [END app]
