from resin_bluemix import get_resin_device, create_device_envar, register
from config import resin_device_uuid

# Get the resin.io device resource via API
resin_device_resource = get_resin_device(resin_device_uuid)

# Register resin device with Bluemix using same ID
r = register(resin_device_resource)

if r.status_code == 201:
    # If new device registered set envars for device
    print "New device registered with bluemix"
    new_device = r.json()
    new_device_id = new_device["id"]
    new_device_token = new_device["password"]
    # set new device ID and token envars
    create_device_envar(
        resin_device_resource['id'], "DEVICE_ID", new_device_id)
    create_device_envar(
        resin_device_resource['id'], "AUTH_TOKEN", new_device_token)
elif r.status_code == 409:
    print "Device is already registered with bluemix"
else:
    print "Error registering device with bluemix, response code " + str(r.status_code)
