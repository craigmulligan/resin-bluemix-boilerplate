#!/usr/bin/python
import time
import random
import json
import ibmiotf.device
from config import organization, device_type, auth_method, device_id, auth_token

client = None

# bluemix connect
try:
    options = {
        "org": organization,
        "type": device_type,
        "id": device_id,
        "auth-method": auth_method,
        "auth-token": auth_token
    }
    client = ibmiotf.device.Client(options)
    client.connect()
    print "Device connect to IBM IoT dashboard - https://" + organization + ".internetofthings.ibmcloud.com/dashboard/#/devices"

except ibmiotf.ConnectionException as e:
    print e


# bluemix publish event
while True:
    try:
        # Let's make some random values for our sensors
        sensor_1 = random.random()å
        sensor_2 = random.random()

        # prefix data with 'd' to distinguish a device published event.
        myData = {"d": {"Sensor one": sensor_1, "Sensor Two": sensor_2}}
        # publish event named status
        client.publishEvent(event="status", msgFormat="json", data=myData)
        time.sleep(1)

    except IOError:
        print "Oops something went wrong with publishing an event"
