FROM nghiant2710/rpi-python

# RUN systemd in container, keeps the container open even if you main process fails.
ENV INITSYSTEM on

# Install deps
RUN apt-get update
RUN apt-get install -y curl

# install ibm IoT python lib
RUN pip install ibmiotf requests

# install ibm-messaging service
RUN curl -LO https://github.com/ibm-messaging/iot-raspberrypi/releases/download/1.0.2/iot_1.0-1_armhf.deb
RUN dpkg -i iot_1.0-1_armhf.deb

# copy current directory into /app
COPY . /app

# run start script when container starts on device
CMD ["bash", "/app/start.sh"]
