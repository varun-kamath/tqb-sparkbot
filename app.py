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

    res = makeWebhookResult(req)

    res = json.dumps(res, indent=4)
    print(res)
    r = make_response(res)
    r.headers['Content-Type'] = 'application/json'
    return r

def makeWebhookResult(req):
    speech = "test"
"""    if req.get("result").get("action") != "search.components":
        return {}
    result = req.get("result")
    parameters = result.get("parameters")
    components = parameters.get("Components")
    number = parameters.get("Number")

    stock = {'Beaglebone':0, 'Raspberry Pi':2, 'Arduino Uno':4}

    if number >= stock[component]:
        speech = "Yes we have " + number + " " + components + " in stock. Do you want to place a request?"
    elif number > 0
        speech = "We only have " + str(stock[components]) + " " + components + " in stock. Do you want to place a request for the same?"
    else
        speech = "I'm sorry we do are out of " + components + ". Contact Lab Admin for Further Queries"
"""
    print("Response:")
    print(speech)

    return {
        "speech": speech,
        "displayText": speech,
        #"data": {},
        # "contextOut": [],
        "source": "varun-kamath/tqb-sparkbot"
    }


if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))

    print "Starting app on port %d" % port

    app.run(debug=True, port=port, host='0.0.0.0')
