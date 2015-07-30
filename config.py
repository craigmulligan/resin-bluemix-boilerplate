# config
import os

# resin config
JWT = os.getenv('JWT')
resin_device_uuid = os.getenv('RESIN_DEVICE_UUID')

# bluemix API config
bluemix_api_key = os.getenv('API_KEY')  
bluemix_api_token = os.getenv('API_TOKEN')

# bluemix config
organization = os.getenv('ORGANIZATION') 
device_type = os.getenv('DEVICE_TYPE')
auth_method = os.getenv('AUTH_METHOD', "token")

# bluemix device config
device_id = os.getenv('DEVICE_ID')  # device envar set on devices first boot
auth_token = os.getenv('AUTH_TOKEN')  # device envar set on devices first boot
