# ensure ibm messaging service has started
service iot start
service iot status
service iot getdeviceid

# run app
cd /usr/src/app && python register.py && python publish.py