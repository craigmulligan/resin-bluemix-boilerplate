# Bluemix and resin.io IoT boilerplate for Raspberry Pi

This is a starting project for anyone using bluemix with an ARM board. It auto registers the device with bluemix and publishes events allowing you to start writing your app right away. 

Resin.io allows one to push docker containers to linux devices with git making the process alot easier to automate at scale. 

Have a look at the code to see how it works but it basically just pushes a container to your device with all the require deps. On first boot it reads your env variables and connects with the bluemix api to create a new device using resin's unique device ID. It then saves the bluemix device credentials as resin device enviroment variables. It then pushes data to your IBM IoT app.

## To RUN 

### Signup with [bluemix](https://console.ng.bluemix.net/)

- Create an app
- Go to Catalog > Internet of things > Internet of Things service > Select application > Create

### Signup with [resin](https://resin.io)
- Create an app
- Download and install image
- If you need more details follow this [link](http://docs.resin.io/#/pages/installing/gettingStarted.md)

### Push code

```
git clone https://github.com/craig-mulligan/Bluemix-resin-boilerplate.git
```
```
git remote add resin <USERNAME>@git.resin.io:<USERNAME>/<APPNAME>.git
```

```
git push resin master
```

### Config

- Got to your resin apps dashboard
- Select enviroment variables tab

Your JSON web token can be found in the preferences section of your resin.io account

JWT = "json web token"

Following variables (can be found on bluemix dashboard if you click show creds on IoT service)

ORGANIZATION = "org"

API_KEY = "apiKey"

API_TOKEN = "apiToken"

DEVICE_TYPE = "eg. RPI2"

![Imgur](http://i.imgur.com/r5LKe5q.png)

### Manage devices and view data stream

The logs will print a link to your IBM IoT dashboard where you can manage your devices and view the data they are publishing. 

IBM IoT Dashboard
[Imgur](http://i.imgur.com/aPm7XkM.png)


### Bonus 

- If you would like to visualize your data, follow this ibm recipe.
https://developer.ibm.com/iotfoundation/recipes/visualize-data/

- It will show you how to pull data from Bluemix and leave you with a cool realtime graph like this. 

![Imgur](http://i.imgur.com/e6LSsz3.png)

