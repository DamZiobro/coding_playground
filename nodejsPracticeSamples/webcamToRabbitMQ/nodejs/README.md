Webcam frames to RabbitMQ
=======

This application allows to grab frames from your webcam (1 FPS) and send them 
to WebServer's (based on nodejs) RabbitMQ queue.

Please note that currently app works only on localhsot as getUserMedia() requires 
HTTPs to grab camera and microphone data. More info here: https://stackoverflow.com/questions/34197653/getusermedia-in-chrome-47-without-using-https

Prerequisities
-----
1. RabbitMQ server runned on your localhost:
```
sudo apt-get install rabbitmq-server
sudo chmod +x rabbitmqadmin
sudo cp rabbitmqadmin /usr/local/bin
sudo rabbitmq-plugins enable rabbitmq_management
sudo service rabbitmq-server start
```
2. Create RabbitMQ local queue 'html.Q.frames' (we will send webcam frames there):
```
./rabbitmqCreateQueue.sh html.Q.frames
```

Usage
-----
1. Run HTTP Web Server on localhost - it will listen on port 3000:
```
node index.js
```
2. Open your WebBrowser in the following address:
```
http://localhost:3000
```
3. Allow access to your webcam and frames should be send from web browser to
   node.js server.
4. Notice that frames should be saved in the following places:
  - /tmp/image.jpg
  - in the rabbitmq queue 'html.Q.frames' - you can check it using command:
```
rabbitmqadmin list queues
```
