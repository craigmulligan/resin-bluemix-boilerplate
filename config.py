# config
import os
# resin config
JWT = os.getenv('JWT') #app envar - javascript web token, used for auth with resin.io api
resin_device_uuid = os.getenv('RESIN_DEVICE_UUID') #app envar - 62 char unique device id provided by resin.io

#bluemix API config 
bluemix_api_key = os.getenv('API_KEY') #app envar 
bluemix_api_token = os.getenv('API_TOKEN') #app envar

# bluemix Device config
organization = os.getenv('ORGANIZATION') #app envar
device_type = os.getenv('DEVICE_TYPE') #app envar - categorizes device on bluemix
auth_method = os.getenv('AUTH_METHOD', "token") #app envar

device_id = os.getenv('DEVICE_ID') # device envar set on devices first boot
auth_token = os.getenv('AUTH_TOKEN') # device envar set on devices first boot