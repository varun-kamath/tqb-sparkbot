#!/usr/bin/env python

import urllib
import requests
import json
import os
import math

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
    if req.get("result").get("action") = "search":
        res = makeWebhookResult1(req)
        return res
    elif req.get("result").get("action") = "RequestAdmin":
        makeWebhookResult2(req)
        return {}
    else:
        return {}

def makeWebhookResult1(req):
    components = req.get("result").get("parameters").get("components")
    number =  req.get("result").get("parameters").get("number")
    
    stock ={'Micro SD Card Reader':4,'Node MCU':4,'BeagleBone Black':4,'GertDuino':1,'NFC Shield':2,'TinkerKit':1,'RaspberryPi 3':1,'L293D Motor Driver':6,'Adafruit Trinket 5V':1,'YwRobot Breadboard Power Supply':3,'GertBoard':1,'PiFace Motor Control Extra (DC+Stepper)':1,'Timer Switch':2,'I2C Motor Driver':2,'Stepper Driver V4.4':2,'Audio Transducer':3,'Vaccuum Pump':1,'Solenoid Valve':1,'Small Brushed DC Motor':1,'Vibrator':2,'Micro Servo Motor':3,'Piezo Buzzer':3,'Buzzer Grove':1,'Water Pump':1,'Vibration Motor Grove':1,'Arduino Motor Shield':3,'Stepper Motor Driver 4988et':3,'Buck Converter':1,'LED Strip':1,'TEMPer USB temperature sensor':1,'Optical Phototransistor Sensor':2,'Linear Current Sensor IC':4,'Load Cell Weight Sensor (0-20Kg)':3,'Dust Sensor Grove':2,'Soil Moisture Sensors':11,'9 Bit Temperature Sensor':5,'Ultrasonic Sensor':10,'IR Sensor':18,'Grove Passive IR Motion Sensor (PIR Sensor)':6,'Thumb Joysticks':2,'Accelerometer':10,'I2C Colour Sensor Grove':2,'Magnetic Switch':3,'Load Cell Weight Sensor (0-6Kg)':1,'Water Sensors':3,'Touch Sensors':2,'Tilt Switch Grove':2,'Grove Alcohol Sensor':1,'Load Cell Weight Sensor (0-50Kg)':2,'Bend Sensor Grove':1,'Grove Relay':2,'Temperature+Humidity sensor Grove':2,'Gas sensor MQ2 Grove':2,'Flow Switch, 15MM, 0.5L/MIN, 10BAR':3,'Accoustic Transciever':3,'Load Sensors':4,'Grove Flame Sensor':1,'Collision Sensor Grove':2,'Rotary Hall Sensor':1,'IR Reflective Sensor Grove':2,'Grove I2C LCD 16x2':2,'Gas sensor MQ2':8,'Humidity Sensors':2,'Temperature Sensor':10,'IR Emitter Grove':1,'Grove Sound Sensor':1,'Grove UV sensor':4,'Position Sensor':1,'Loudness Sensor Grove ':2,'Air Quality Sensor Grove':2,'LDR Sensor Grove ':1,'Temperature Sensor Grove':1,'Line Finder Grove':1,'Pressure Sensors Honeywell':6,'Pressure Sensors 10KPa':10,'Grove Encoder':1,'Inch Bend Sensor':1,'Ultrasonic Sensor Grove':5,'Microphone':4,'Grove Water Sensor':2,'Grove Barometer':1,'IR proximity (Gap) Sensor':22,'Hall Sensor':4,'GPS Trucker':1,'Light Sensor Grove ':1,'Optical Proximity Sensor':2,'LDR':3,'Adapter 12V 1A':18,'Solar Cell 5.5V 540mA':1,'AA Rechargeable Batteries 1.2V':25,'Switching Adapter':1,'Battery Charger':1,'Battery Case 4 Cell ':2,'AAA Rechargeable Batteries 1.2V':32,'Battery Case 2 Cell ':31,'Rechargeable Duracell Ni-MH Battery 9V':3,'NFC Smart Card Reader':1,'Solar Cell 5.5V 100mA':1,'Adapter 5V 10A':1,'GPS Module':2,'CMOS Battery Holder':4,'Wireless Charging Boards':2,'DB9 Connectors':2,'Plugs ':2,'Battery Adapter Plug':1,'Grove Serial Camera Kit':1,'WiFi Module':5,'IR Receiver Grove':1,'HC05 Bluetooth Module':12,'Logitech C525 HD Webcam':1,'Raspberry Pi 2':8,'TI SensorTag Development Kit':7,'MultiBand Swivel Mount Dipole Antenna':4,'5V 2A Raspberry Pi Adapters':8,'Arduino Proto Shield':3,'Arduino Uno':2,'PiFace 16x2 LCD Display (for Raspberry Pi)':1,'PiFace Real Time Clock (for Raspberry Pi)':1,'4 Port USB Hub':1,'Spark Core WiFi Development Kit':1,'Xbee ZigBee Module':10,'Lightning and Surge Protection 150W':1,'Dymo LabelWriter':1,'RJ45 Connector':10,'Ammeter 100uA':1,'Arduino Robot':1,'mbed LPC1114FN28 32-Bit MCU':1,'Grove Arduino Starter Kit':2,'Pi NoIR Camera Board':4,'Arduino Base Shield':2,'Arduino CAN Bus Shield':1,'Arduino Energy Shield':2,'Arduino ZigBee Shield':1,'Seeed Lipo Charger Circuit':1,'LinkIt ONE':1,'LinkIt Connect':2,'Explore-NFC':2,'Universal Adapter (3,4.5,5,6,7.5,9,12V-1.5A)':1,'LoRa':1,'Alamore Arduino Compatible Paspberry Pi Plate':1,'Digital Multimeter':1,'USB to UART Converter':7,'ESP32':1,'5V 2A Adapters':1,'AdaFruit Flora Development kit':1,'Sparkfun Cryptoshield':1,'Tool Kit':1,'LM2904P OpAmp':15,'Starter Bundle Harness':3,'Raspberry Pi 3 Case':1,'ATTiny 13A-PU':19,'Strontium microSD Card Set':4,'SanDisk microSD Card Adapter':10,'ATTiny 84A':20,'LM258NG OpAmp':5,'ATTiny 4313-SU':20,'LM339AN Quad Differential Comparator OpAmp':5,'OptoCoupler, Logic Gate O/P 5.3KV':5,'LM2901N Comparator OpAmp':5,'CMOS Timer ':5,'16MHz Crystal':5,'IR Emitter':10,'ATMega 328P SMD':1,'Adjustable Buck Converter':2,'Screw Terminlas':7,'4 Bit Logic Level Converter':3,'Headphones':4,'Relay':2,'Vernier Calliper':1,'BLE Nano Kit (Bluetooth Low Energy)':2,'ODROID Hard Kernel':1,'CY5671 PRoC BLE Module':3,'PMIC Energy Harvesting':3,'RF TXRX+MCU Bluetooth':3,'LED RGB Strip':3,'Yellow EL Tape':2,'Green EL Tape':2,'Red EL Tape':1,'8x8 Square LED Matrix':1,'Grove EL Driver':3,'Grove LED Red':2,'Grove LED Green':1,'4 Digit Grove Display':2,'LED Strip Driver':2,'14 Segment Driver':2,'Laser Motor Emitter':2,'Grove Blue LED':1,'Grove White LED':2,'Grove LED Bar':3,'External Antenna 2.4GHz':2,'Bluetooth BLE Modules ':9,'Grove NFC Tags':6,'Grove Bluetooth Low Energy (BLE) Modules':2,'EMW3162 WiFi Module External':3,'RFID Tag 125kHz':25,'ESP8266':14,'NFC Tags':12,'ESP8266 WiFi Module':8,'RFID Reader Grove':1,'RFID Reader':10,'RFID Reader UART Grove':2,'RFID Book Tags 13.56MHz':1,'Long Range RF Link Kits':1,'RFID Reader 13.56MHz':1,'RFID Reader Grove 125KHz':3,'Grove - Universal 4 Pin Unbuckeled Cable':60,'Grove - Universal 4 Pin Buckeled Cable':25,'Audio Jack to 9V Connector':3,'HDMI Cable':4,'Grove - Branch cable':10,'Grove - 4 Pin Female Jumper to 4 Pin Connector':10,'Power Converter':2,'Vaccum Pump':1,'Audio cable - 3.5 mm Jack':1,'RJ45 Cable':3,'Qualcom Gimball Beacon BLF Tag':13,'RJ45 to Parallel Cable':1,'Power Cable':1,'Jumper Connector':40,'USB Cable':3,'USB to PS2 Cable':1,'Bulb Holder':2,'Speaker Cable':2,'USB to Jumper Cable':2,'VGA to Parallel cable':1,'USB to USB Mini Cable':1,'RJ45 to DB9 Connector':1,'USB Type A to DB9 Connector':1,'20 Pin FRC Cable for Raspberry Pi':1,'PiView HDMI to VGA Converter for Raspberry Pi':1,'1 Watt LED':16,'Panel Mount Miniature Jack':8}
    
    if int(number) <= 0:
        speech = "Good Joke."
    elif stock[components] == 0:
        speech = "We are out of " + components + "(s). Please contact lab admin for further queries."
    elif int(number) <= stock[components]:
        speech = "yes we have " + number + " " + components + "(s) . Should i register a request?"
    elif int(number) > stock[components]:
        speech = "we only have " + str(stock[components]) + " " + components + "(s) . Should i register a request for the same?"
    
    print("Response:")
    print(speech)

    return {
        "speech": speech,
        "displayText": speech,
        #"data": {"slack": slack_message, "facebook": facebook_message},
        # "contextOut": [],
        "source": "tqb-sparkbot"
    }

def makeWebhookResult2(req):
    ACCESS_TOKEN = 'M2U2MmQ1N2ItMTgxNi00NjM3LWIyZmEtNmI3NjI5ZjQzMTNjYWM5Nzk4YTItMDE4'
    headers = {'Authorization': 'Bearer ' + ACCESS_TOKEN}
    data = {'roomId': 'Y2lzY29zcGFyazovL3VzL1JPT00vMDQ4NDMwNDUtMmYyMC0zYmZlLTlkY2QtMWZlYTg4MzQzYzVm',
                           'text': 'Hello StackOverflow'}
    resp = requests.post(url='https://api.ciscospark.com/v1/messages', data=data, headers=headers)


if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))

    print "Starting app on port %d" % port

    app.run(debug=False, port=port, host='0.0.0.0')
