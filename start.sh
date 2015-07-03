# ensure ibm messaging service has started
service iot start
service iot status
service iot getdeviceid
# run app
python /app/register.py && python /app/publish.py