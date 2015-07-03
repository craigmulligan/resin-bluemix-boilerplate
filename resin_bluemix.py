import time, random, json
import requests
from requests.auth import HTTPBasicAuth
from config import JWT, bluemix_api_key, bluemix_api_token, organization, device_type, resin_device_uuid

# Gets device resource from resin
def get_resin_device(uuid):
	url = "https://api.resin.io/ewa/device?$filter=uuid%20eq%20'"+ uuid +"'"
	headers = {'Content-type': 'application/json', 'Authorization': 'Bearer ' + JWT}
	r = requests.get(url, headers=headers)
	if r.status_code == 200:
		resin_device = r.json()['d'][0]
		print "This is a resin device with name: " + resin_device['name'] + 'and ID: ' + str(resin_device['id'])
		return resin_device
	else: 
		print 'Error connecting to resin.io api, response code ' + str(r.status_code)

# Creates device envar for bluemix device credentials, allowing config to persist threw updates
def create_device_envar(device_id, key, value):
	url = "https://api.resin.io/ewa/device_environment_variable"
	data = {
	  "device": device_id,
	  "env_var_name": key,
	  "value": value
	}
	headers = {'Content-type': 'application/json', 'Authorization': 'Bearer ' + str(JWT)}
	r = requests.post(url, data=json.dumps(data), headers=headers)
	if r.status_code == 201:
		print "New device envar - " + str(key) + ":" + str(value) + " successfully created"
	else: 
		print 'Error creating resin.io envar ' + str(key) + ', response code ' + str(r.status_code)

# registers device with bluemix using resin device ID
def register(device):
 	# Make both our resin db and bluemix db have same id for devices
	url = "https://" + str(organization) + ".internetofthings.ibmcloud.com/api/v0001/devices"
	data = {
		"type": device_type,
		"id": device['id'],
		"metadata": {
		  "address": {
		    "number": 29,
		    "street": "Acacia Road"
		  }
		}
	}
	headers = {'Content-type': 'application/json'}

	r = requests.post(url, data=json.dumps(data), headers=headers, auth=HTTPBasicAuth(bluemix_api_key, bluemix_api_token))
	return r