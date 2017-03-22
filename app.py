#!/usr/bin/env python

import urllib
import json
import os

from flask import Flask
from flask import request
from flask import make_response

# Flask app should start in global layout
app = Flask(__name__)


@app.route('/webhook', methods=['POST'])
def webhook():
    req = request.get_json(silent=True, force=True)

    print("Request:")
    print(json.dumps(req, indent=4))

    res = processRequest(req)

    res = json.dumps(res, indent=4)
    # print(res)
    r = make_response(res)
    r.headers['Content-Type'] = 'application/json'
    return r


def processRequest(req):
    if req.get("result").get("action") != "search":
        return {}

    res = makeWebhookResult(req)
    return res


def makeWebhookResult(req):
    components = req.get("result").get("parameters").get("components")
    number =  req.get("result").get("parameters").get("number")
    
    stock = {'a':3, 'b':5, 'c':2, 'd':8, 'e':6}
    
    speech = "test"
    
    if int(str(stock[components])) > number:
        speech = speech + "yes we have " + number + " " + components
    #elif int(stock[components]) < number:
    #    speech = "no we dont have " + number + " " + components

    speech = speech + " test"
    
    print("Response:")
    print(speech)

    return {
        "speech": speech,
        "displayText": speech,
        #"data": {"slack": slack_message, "facebook": facebook_message},
        # "contextOut": [],
        "source": "apiai-weather-webhook-sample"
    }


if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))

    print "Starting app on port %d" % port

    app.run(debug=False, port=port, host='0.0.0.0')
